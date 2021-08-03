class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heap = []

        for i in range(len(values)):
            heappush(heap, (-values[i], labels[i]))

        if use_limit == 0 or num_wanted == 0:
            return 0

        used = {}
        ret = 0
        while len(heap) > 0:
            heap_item = heappop(heap)
            value = heap_item[0]
            label = heap_item[1]

            used[label] = used.get(label, 0) + 1
            if used[label] <= use_limit:
                ret += (-value)
                num_wanted -= 1

                if num_wanted == 0:
                    break

        return ret
