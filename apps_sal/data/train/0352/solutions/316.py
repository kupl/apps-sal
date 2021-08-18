class Solution:
    def match(self, small, big):
        mismatch = 0
        i = 0
        while i < len(small):
            j = i + mismatch

            if small[i] == big[j]:
                i += 1
                continue
            elif not mismatch:
                mismatch = 1
            elif mismatch == 1:
                return False

        return True

    def longestStrChain(self, words: List[str]) -> int:

        if len(words) == 1:
            return 1
        len_counts = {}
        min_len = 17

        for w in words:
            l = len(w)
            if l not in len_counts:
                len_counts[l] = [w]
                if l < min_len:
                    min_len = l
            else:
                len_counts[l].append(w)

        chains = {}

        for w in len_counts[min_len]:
            chains[w] = 1
        ans = -1

        keys = sorted(list(len_counts.keys()))
        prev_len = keys[0]
        for l in keys[1:]:

            poss = len_counts[l]
            if l != prev_len + 1:
                prev_len = l

                for w in poss:
                    if w not in chains:
                        chains[w] = 1

                continue

            poss_last = len_counts[prev_len]

            for w in poss:
                if w not in chains:
                    chains[w] = 1

                for last in poss_last:
                    if self.match(last, w):
                        chains[w] = max(chains[w], chains[last] + 1)

            prev_len = l
        return max(chains.values())
