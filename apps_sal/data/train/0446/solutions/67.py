class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counted_arr = dict(Counter(arr))
        counted_arr = sorted(list(counted_arr.items()), key=lambda kv: kv[1], reverse=False)
        print(counted_arr)

        while k > 0 and len(counted_arr) > 0:
            val = counted_arr[0]
            freq = val[1]
            k -= freq

            if k >= 0:
                counted_arr.pop(0)

        return len(counted_arr)
