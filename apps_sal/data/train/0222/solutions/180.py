class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        setA = set(A)
        answer = 0
        max_ = A[-1]
        visited = set()
        queue = collections.deque()
        for i in range(len(A) - 1):
            curr1 = A[i]
            for j in range(i + 1, len(A)):
                curr2 = A[j]
                if curr1 + curr2 in setA:
                    queue.append((curr1, curr2))
        while queue:
            (num1, num2) = queue.popleft()
            if (num1, num2) in visited:
                continue
            visited.add((num1, num2))
            sum_ = num1 + num2
            l = 2
            while sum_ in setA and sum_ <= max_:
                (num1, num2) = (num2, sum_)
                sum_ = num1 + num2
                visited.add((num1, num2))
                l += 1
            answer = max(answer, l)
        return answer
