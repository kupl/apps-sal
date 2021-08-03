class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        fw = [arr[0]]
        bw = [arr[-1]]

        cur_max = max_so_far = arr[0]
        for num in arr[1:]:
            cur_max = max(cur_max + num, num)
            max_so_far = max(max_so_far, cur_max)
            fw.append(cur_max)

        cur_max = arr[-1]
        for num in arr[:-1][::-1]:
            cur_max = max(cur_max + num, num)
            max_so_far = max(max_so_far, cur_max)
            bw.append(cur_max)
        bw = bw[::-1]

        for i in range(1, len(arr) - 1):
            max_so_far = max(max_so_far, fw[i - 1] + bw[i + 1])
        return max_so_far
