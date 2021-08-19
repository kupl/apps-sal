class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answer = 0
        avg = average(arr[0:k])
        prev_el = arr[0]
        if avg >= threshold:
            answer += 1
        for i in range(k, len(arr)):
            new_avg = (avg * k - prev_el + arr[i]) / k
            if new_avg >= threshold:
                answer += 1
            avg = new_avg
            prev_el = arr[i - k + 1]
        return answer


def average(l):
    return sum(l) / len(l)
