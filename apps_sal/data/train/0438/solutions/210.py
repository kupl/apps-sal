class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        a = [0]*n
        c = [0]*n
        for i in range(n):
            a[i] = -1
            c[i] = -1
        res = -1
        have_m = 0
        def find_root(i):
            while a[i] != i:
                i = a[i]
            return i
        step = 0
        for pos in arr:
            step+=1
            pos -= 1
            if pos<n-1 and a[pos+1]!=-1:
                a[pos+1] = pos
                a[pos] = pos
                c[pos] = c[pos+1]+1
                if c[pos+1] == m:
                    have_m-=1
                if c[pos] == m:
                    have_m+=1
            else:
                a[pos] = pos
                c[pos] = 1
                if c[pos] == m:
                    have_m+=1
            if pos>0 and a[pos-1]!=-1:
                a[pos] = find_root(pos-1)
                if c[pos] == m:
                    have_m -= 1
                if c[a[pos]] == m:
                    have_m -= 1
                c[a[pos]] += c[pos]
                if c[a[pos]] == m:
                    have_m+=1
            if have_m:
                res = step
        return res
                

