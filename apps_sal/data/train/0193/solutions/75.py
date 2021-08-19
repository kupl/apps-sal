class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        arr_mc = collections.Counter(arr).most_common()
        print(arr_mc)
        for i in range(len(arr_mc)):
            total_count += arr_mc[i][1]
            if total_count >= len(arr) / 2:
                return i + 1
