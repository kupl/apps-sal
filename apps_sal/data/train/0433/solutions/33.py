class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        averages = []
        first = True
        sum_avg = 0
        for i in range(len(arr) - (k - 1)):
            if first:
                for j in range(k):
                    sum_avg += arr[i + j]
                first = False
            else:
                sum_avg -= arr[i - 1]
                sum_avg += arr[i + (k - 1)]
            averages.append(sum_avg / k)
        averages.sort(reverse=True)
        i = 0
        while i < len(averages) and averages[i] >= threshold:
            i += 1
        return i
