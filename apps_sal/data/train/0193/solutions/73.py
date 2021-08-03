class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #         if not arr:
        #             return 0

        #         ceil = len(arr) / 2.0

        #         count = collections.Counter(arr)
        #         sort = count.most_common()
        #         sum = 0
        #         for idx,val in enumerate(sort):
        #             sum += val[1]
        #             if sum >= ceil:
        #                 return idx+1

        #         return idx+1
        if not arr:
            return 0
        counter = collections.Counter(arr)
        max_val = max(counter.values())

        buckets = [0] * (max_val + 1)

        for count in list(counter.values()):
            buckets[count] += 1

        set_size = 0
        arr_num_to_remove = len(arr) // 2
        bucket = max_val

        while arr_num_to_remove > 0:
            max_need_from_bucket = math.ceil(arr_num_to_remove / bucket)
            set_size_increase = min(buckets[bucket], max_need_from_bucket)
            set_size += set_size_increase
            arr_num_to_remove -= set_size_increase * bucket
            bucket -= 1

        return set_size
