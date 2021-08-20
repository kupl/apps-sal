class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        l = len(arr)
        if l == 0:
            return 0
        (frontview, backview, sumfront, sumback) = ([0] * l, [0] * l, [0] * l, [0] * l)
        (frontview[0], backview[-1], sumfront[0], sumback[-1]) = (max(0, arr[0]), max(0, arr[-1]), arr[0], arr[-1])
        for i in range(1, l):
            frontview[i] = max(0, frontview[i - 1] + arr[i])
            backview[l - 1 - i] = max(0, backview[l - i] + arr[l - 1 - i])
            sumfront[i] = sumfront[i - 1] + arr[i]
            sumback[l - 1 - i] = sumback[l - i] + arr[l - 1 - i]
        sum_arr = sum(arr)
        base = 10 ** 9 + 7
        if k == 1:
            return max(frontview) % base
        elif sum_arr <= 0:
            result1 = max(max(frontview), frontview[-1] + backview[0]) % base
            result2 = max(sumfront) + max(sumback)
            print((result1, result2))
            return max(result1, result2) % base
        else:
            result1 = max(max(frontview), frontview[-1] + backview[0])
            result2 = sum_arr * (k - 2) + max(sumfront) + max(sumback)
            if result1 < result2:
                return result2 % base
            else:
                return result1 % base
