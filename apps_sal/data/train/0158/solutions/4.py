from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def swapPos(string):
            i = 0
            while string[i] == B[i]:
                i += 1
            for j in range(i+1, length):
                if string[j] == B[i]:
                    yield string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]

        dq = deque([(A, 0)])
        visited = set(A)
        length = len(A)
        while dq:
            string, dist = dq.popleft()
            if string == B:
                return dist
            for s2 in swapPos(string):
                if s2 not in visited:
                    dq.append((s2, dist+1))
                    visited.add(s2)
