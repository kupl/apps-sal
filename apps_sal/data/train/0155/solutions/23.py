class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        def find_longest_l(pos, d):
            if pos - 1 < 0 or arr[pos - 1] > arr[pos]:
                return pos
            i = pos
            while i > 0 and abs(pos - i) < d and (arr[i - 1] < arr[pos]):
                i -= 1
            return i

        def find_longest_r(pos, d):
            if pos + 1 >= len(arr) or arr[pos + 1] > arr[pos]:
                return pos
            i = pos
            while i < len(arr) - 1 and abs(pos - i) < d and (arr[i + 1] < arr[pos]):
                i += 1
            return i

        def jump(pos, number_of_locations, seen):
            maximum_locations = number_of_locations
            L = find_longest_l(pos, d)
            R = find_longest_r(pos, d)
            for i in range(L, R + 1):
                if i == pos:
                    continue
                if i not in seen:
                    jumps_to_i = jump(i, number_of_locations, seen)
                    maximum_locations = max(maximum_locations, jumps_to_i + 1)
                else:
                    jumps_to_i = seen[i]
                    maximum_locations = max(maximum_locations, jumps_to_i + 1)
            seen[pos] = maximum_locations
            return maximum_locations
        indices = [(i, arr[i]) for i in range(len(arr))]
        indices.sort(key=lambda x: x[1], reverse=True)
        seen = {}
        return max((jump(x[0], 1, seen) for x in indices))
