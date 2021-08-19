class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        sum_ = [0]
        for num in A:
            sum_.append(sum_[-1] + num)
        result = len(A) + 1
        deque = []
        for (i, num) in enumerate(sum_):
            while deque and num <= sum_[deque[-1]]:
                deque.pop()
            while deque and num - sum_[deque[0]] >= K:
                result = min(result, i - deque[0])
                deque.pop(0)
            deque.append(i)
        return result if result != len(A) + 1 else -1
