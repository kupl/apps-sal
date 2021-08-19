from math import ceil


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        brr = []
        count = 1
        cur = arr[0]
        for i in range(1, len(arr)):
            if cur == arr[i]:
                count += 1
            else:
                brr.append([cur, count])
                cur = arr[i]
                count = 1
        brr.append([cur, count])
        brr.sort(key=lambda x: x[1], reverse=True)
        temp = 0
        temp1 = 0
        for i in brr:
            if temp >= ceil(len(arr) / 2):
                return temp1
            temp1 += 1
            temp += i[1]
        return 1
