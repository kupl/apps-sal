class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        checked, answer = [], 0
        count_d, total = [], 0

        if len(arr) == len(set(arr)):
            return int(len(arr) / 2)

        for num in arr:
            if num not in checked:
                count_d.append(arr.count(num))
                checked.append(num)

        count_d.sort()

        for d in range(1, len(count_d) + 1):
            total += count_d[-d]
            answer += 1
            if total >= len(arr) / 2:
                return answer
