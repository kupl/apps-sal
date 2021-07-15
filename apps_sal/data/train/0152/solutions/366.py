class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        if m < 2: return -1
        pos.sort()
        avg = (pos[-1]-pos[0]+1)//(m-1)+1
        #boolean
        def check(f):
            nonlocal pos, m
            cnt = 0
            pidx = 0
            for i in range(1, len(pos)):
                if (pos[i]-pos[pidx]+1) >= f:
                    cnt += 1
                    pidx = i
            #print(\"cnt:\", cnt)
            return cnt >= m-1

        l, r = 1, avg
        #print(\"l:\", l, \"r:\", r)
        while l+1<r:
            mid = l+(r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        #print(\"l:\", l, \"r:\", r)
        if check(r): return r-1
        else: return l-1



