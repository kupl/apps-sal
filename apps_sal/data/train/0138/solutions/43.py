class Solution:

    def getMaxLen(self, arr: List[int]) -> int:
        i = 0
        while i <= len(arr) - 1 and arr[i] == 0:
            i += 1
        arr = arr[i:]
        if len(arr) == 0:
            return 0
        i = len(arr) - 1
        while i <= len(arr) - 1 and arr[i] == 0:
            i -= 1
        arr = arr[:i + 1]
        if len(arr) == 0:
            return 0
        array = []
        low = 0
        high = 0
        ans = []
        while low < len(arr):
            while high < len(arr) and arr[high] != 0:
                high += 1
            if high == len(arr) - 1:
                break
            else:
                array.append(arr[low:high])
                while high < len(arr) and arr[high] == 0:
                    high += 1
                low = high
        for a in array:
            if len(a) == 0:
                continue
            else:
                total = 0
                first = 0
                last = 0
                for i in range(len(a)):
                    if a[i] < 0:
                        total += 1
                if total % 2 == 0:
                    ans.append(len(a))
                else:
                    i = 0
                    while a[i] > 0:
                        i += 1
                    first = len(a) - (i + 1)
                    i = len(a) - 1
                    while a[i] > 0:
                        i -= 1
                    last = i
                ans.append(max(first, last))
        ma = 0
        for i in ans:
            if i > ma:
                ma = i
        return ma
