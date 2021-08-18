class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def make_mono_stack(sorted_idxes):
            result = [None] * len(sorted_idxes)
            stack = []
            for idx in sorted_idxes:
                while stack and idx > stack[-1]:
                    result[stack.pop()] = idx
                stack.append(idx)
            return result

        n = len(A)
        sorted_idxes = sorted(list(range(n)), key=lambda i: A[i])
        odd_next = make_mono_stack(sorted_idxes)
        sorted_idxes.sort(key=lambda i: A[i], reverse=True)
        even_next = make_mono_stack(sorted_idxes)

        odd_can_reach_from_idx = [False] * n
        even_can_reach_from_idx = [False] * n
        odd_can_reach_from_idx[-1] = even_can_reach_from_idx[-1] = True

        for i in range(len(A) - 2, -1, -1):
            if odd_next[i] is not None:
                odd_can_reach_from_idx[i] = even_can_reach_from_idx[odd_next[i]]
            if even_next[i] is not None:
                even_can_reach_from_idx[i] = odd_can_reach_from_idx[even_next[i]]
        return sum(odd_can_reach_from_idx)
