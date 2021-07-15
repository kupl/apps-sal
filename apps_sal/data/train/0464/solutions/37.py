class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            arr = [0]*n
            arr[0] = 1
            arr[1] = 3
            for i in range(2,n):
                arr[i] = arr[i-1] + 2
            if n % 2 != 0:
                ans = 0
                i = 0
                j = len(arr)-1
                while i < j:
                    ans += (arr[j]-arr[i])//2
                    i += 1
                    j -= 1
                return ans
            else:
                ans = 0
                n = n // 2
                i = 1
                count = 0
                ans = 0
                while count < n:
                    ans += i
                    i += 2
                    count += 1
                return ans
