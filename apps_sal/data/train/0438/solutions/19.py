class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        l = len(arr)
        x = [[] for x in range(l+1)]
        if l == m:
            return l

        last = -1
        lens = [0 for x in range(l+1)]
        for i in range(0,l):
            cur = arr[i]
            right = []
            left = []
            if cur+1 < l+1:
                right = x[cur+1]
            if cur-1 >= 0:
                left = x[cur-1]

            lv = rv = cur
            ss = 1
            if left:
                lv = left[1]
                ss += left[0]
                lens[left[0]] -=1     
                if left[0] == m:
                    last = i
            if right:
                rv = right[2]
                ss += right[0]
                lens[right[0]] -=1
                if right[0] == m:
                    last = i
            lens[ss]+=1
            x[lv] = [ss,lv,rv]
            x[rv] = [ss,lv,rv]

        return last
