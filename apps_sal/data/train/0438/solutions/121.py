class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = len(arr)
        length_to_index = defaultdict(set)
        state = [(0, 0) for i in range(length + 2)]
        ans = -1
        for (step, index) in enumerate(arr):
            if state[index - 1] == (0, 0) and state[index + 1] == (0, 0):
                state[index] = (1, 1)
                length_to_index[1].add(index)
            elif state[index + 1] == (0, 0):
                L = state[index - 1][0] + 1
                state[index] = (L, 1)
                state[index - L + 1] = (1, L)
                length_to_index[L - 1].remove(index - L + 1)
                length_to_index[L].add(index - L + 1)
            elif state[index - 1] == (0, 0):
                L = state[index + 1][1] + 1
                state[index] = (1, L)
                state[index + L - 1] = (L, 1)
                length_to_index[L - 1].remove(index + 1)
                length_to_index[L].add(index)
            else:
                l_left = state[index - 1][0]
                l_right = state[index + 1][1]
                L = l_left + l_right + 1
                state[index - l_left] = (1, L)
                state[index + l_right] = (L, 1)
                length_to_index[l_right].remove(index + 1)
                length_to_index[l_left].remove(index - l_left)
                length_to_index[L].add(index - l_left)
            if length_to_index[m]:
                ans = step + 1
        return ans
