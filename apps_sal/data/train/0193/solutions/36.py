class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()

        counts = []
        current_run = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                current_run += 1
                continue
            counts.append(current_run)
            current_run = 1
        counts.append(current_run)

        counts.sort(reverse=True)

        numbers_removed_from_arr = 0
        set_size = 0
        for count in counts:
            numbers_removed_from_arr += count
            set_size += 1
            if (numbers_removed_from_arr >= len(arr) // 2):
                break

        return set_size
