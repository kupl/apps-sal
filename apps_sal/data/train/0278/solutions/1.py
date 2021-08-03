class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:

        heaps, total = [[], [], []], 0

        for digit in digits:
            total += digit
            heapq.heappush(heaps[digit % 3], str(digit))

        if r := (total % 3):
            if heaps[r]:
                heapq.heappop(heaps[r])
            elif len(heaps[-r]) > 1:
                heapq.heappop(heaps[-r])
                heapq.heappop(heaps[-r])

        if any(heaps):
            return str(int(''.join(sorted(sum(heaps, []), reverse=True))))
        return ''
