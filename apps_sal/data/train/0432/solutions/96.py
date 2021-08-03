class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        h = []
        for num in nums:
            tmp = []
            found = False
            while h:
                max_idx, min_idx = heapq.heappop(h)
                if max_idx > num - 1:
                    tmp.append((max_idx, min_idx))
                    break

                if max_idx == num - 1:
                    found = True
                    if max_idx - min_idx + 2 == k:
                        break

                    heapq.heappush(h, (max_idx + 1, min_idx))

                    break
                tmp.append((max_idx, min_idx))

            for item in tmp:
                heapq.heappush(h, item)

            if found:
                continue

            if k != 1:
                heapq.heappush(h, (num, num))

        return not h
