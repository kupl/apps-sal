class Solution:
    def maxTurbulenceSize(self, a: List[int]) -> int:
        mx = 1
        cnt = 1
        n = len(a)
        if(n == 1):
            return 1
        i = j = 0
        if(a[i] < a[i + 1]):
            f = 0
        elif(a[i] > a[i + 1]):
            f = 1
        else:
            while(j < n - 1):
                if(a[j] != a[j + 1]):
                    break
                j += 1
            i = j
            if(j == n - 1):
                return 1
            if(a[i] < a[i + 1]):
                f = 1
                cnt += 1
            elif(a[i] > a[i + 1]):
                f = 0
                cnt += 1
        for i in range(j, n - 1, 1):
            if(a[i] > a[i + 1]):
                if(f == 1):
                    cnt += 1
                    f = 0
                else:
                    mx = max(mx, cnt)
                    cnt = 2
                    f = 0
            elif(a[i] < a[i + 1]):
                if(f == 0):
                    cnt += 1
                    f = 1
                else:
                    mx = max(mx, cnt)
                    cnt = 2
                    f = 1
            else:
                mx = max(mx, cnt)
                cnt = 1
                j = i
                while(j < n - 1):
                    if(a[j] != a[j + 1]):
                        break
                    j += 1
                i = j
                if(j == n - 1):
                    break
                if(a[i] < a[i + 1]):
                    f = 1
                    cnt += 1
                elif(a[i] > a[i + 1]):
                    f = 0
                    cnt += 1
            mx = max(cnt, mx)

        return mx
