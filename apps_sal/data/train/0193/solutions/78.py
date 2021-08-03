class Solution:

    def check(self, arr, to_remove):
        return len(tuple(filter(lambda x: not to_remove.contains(x), arr))) <= len(arr) / 2

    def minSetSize(self, arr: List[int]) -> int:
        all_nums = set(arr)
        freq = {n: 0 for n in all_nums}
        for num in arr:
            freq[num] += 1

        nums_by_count = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        remove_count = 0
        result = 0
        half = len(arr) / 2
        for item in nums_by_count:
            num, count = item
            remove_count += count
            result += 1
            if remove_count >= half:
                return result
