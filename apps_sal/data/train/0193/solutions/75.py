class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        #         total_count = len(arr)
        #         values = set(arr)
        #         values = list(values)
        #         possible_combinations = []

        #         for i in values:
        #             possible_combinations.append([i,arr.count(i)])

        #         result = [seq for i in range(len([item[1] for item in possible_combinations]), 0, -1) for seq in itertools.combinations([item[1] for item in possible_combinations], i) if sum(seq) >= total_count//2]

        #         return min(len(i) for i in result)

        total_count = 0
        arr_mc = collections.Counter(arr).most_common()

        print(arr_mc)

        for i in range(len(arr_mc)):
            total_count += arr_mc[i][1]
            if total_count >= len(arr) / 2:
                return i + 1
