class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        n = len(A)
        #A[2*i+1] = 2*A[2*i]
        # [-2,-4,2,4]
        #A[1] == 2*A[0]
        #A[3] == 2*A[2]
        neg = sorted(list([x for x in A if x < 0]))
        pos = sorted(list([x for x in A if x > 0]), reverse=True)
        nl, pl = len(neg), len(pos)
        if nl % 2 or pl % 2:
            return False
        d1 = collections.Counter(neg)
        cnt = 0
        for i in range(nl):
            if d1[2 * neg[i]] > 0:
                d1[2 * neg[i]] -= 1
                d1[neg[i]] -= 1
                cnt += 1
        if cnt < nl // 2:
            return False
        d2 = collections.Counter(pos)
        cnt = 0
        for i in range(pl):
            if d2[2 * pos[i]] > 0:
                print((pos[i] * 2, pos[i]))
                d2[2 * pos[i]] -= 1
                d2[pos[i]] -= 1
                cnt += 1
        if cnt < pl // 2:
            return False
        return True
