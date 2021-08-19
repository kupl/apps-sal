class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == 0 and b == 0 and (c == 0):
            return ''
        res = ''
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        prev_val = 0
        prev_char = ''
        while heap:
            (v, char) = heapq.heappop(heap)
            if prev_val < 0:
                heapq.heappush(heap, (prev_val, prev_char))
            if abs(v) >= 2:
                if abs(v) > abs(prev_val):
                    res += char * 2
                    v += 2
                else:
                    res += char
                    v += 1
            elif abs(v) == 1:
                res += char
                v += 1
            elif abs(v) == 0:
                break
            prev_val = v
            prev_char = char
        return res
