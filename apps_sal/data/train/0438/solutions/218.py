class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        left = [0]*(n+2)
        right = [0]*(n+2)
        def getlength(x):
            return right[x]-x+1
        count = 0
        res = -1
        for i in range(n):
            x = arr[i]
            if left[x-1] and right[x+1]:
                if getlength(left[x-1]) == m:
                    count -= 1
                if getlength(x+1) == m:
                    count -= 1
                right[left[x-1]] = right[x+1]
                left[right[x+1]] = left[x-1]
                if getlength(left[x-1]) == m:
                    count += 1
            elif left[x-1]:
                if getlength(left[x-1]) == m:
                    count -= 1
                right[left[x-1]] = x
                left[x] = left[x-1]
                if getlength(left[x-1]) == m:
                    count += 1
            elif right[x+1]:
                if getlength(x+1) == m:
                    count -= 1
                left[right[x+1]] = x
                right[x] = right[x+1]
                if getlength(x) == m:
                    count += 1
            else:
                left[x] = x
                right[x] = x
                if m == 1:
                    count += 1
            if count > 0:
                res = i + 1
        return res
