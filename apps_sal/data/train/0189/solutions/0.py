class Solution:
    def preferences_to_scores(self, preferences):
        scores = {}
        for u, up in enumerate(preferences):
            for s, v in enumerate(up):
                scores[(u, v)] = s
        return scores

    def unhappy_friends(self, scores, a, b):
        ret = set()
        for ai, aa in enumerate(a):
            af = a[1 - ai]
            for bi, bb in enumerate(b):
                bf = b[1 - bi]
                if scores[(aa, bb)] < scores[(aa, af)] and scores[(bb, aa)] < scores[(bb, bf)]:
                    ret.add(aa)
                    ret.add(bb)
        return ret

    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        scores = self.preferences_to_scores(preferences)
        ret = set()
        for i, a in enumerate(pairs):
            for j in range(i):
                b = pairs[j]
                ret |= self.unhappy_friends(scores, a, b)
        return len(ret)
