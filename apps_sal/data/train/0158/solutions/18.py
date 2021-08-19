class Solution:

    def bfs(self, A: str, B: str):
        if A == B:
            return 0
        n = len(A)
        q = []
        visited = set()
        q.append((B, 0, 0))
        while q:
            (processed, idx, swaps) = q.pop(0)
            visited.add(processed)
            while processed[idx] == A[idx]:
                idx += 1
            for i in range(idx + 1, n):
                if A[idx] == processed[i]:
                    new_processed = processed[:idx] + processed[i] + processed[idx + 1:i] + processed[idx] + processed[i + 1:]
                    if A == new_processed:
                        return swaps + 1
                    if new_processed not in visited:
                        q.append((new_processed, idx + 1, swaps + 1))
        return 0

    def kSimilarity(self, A: str, B: str) -> int:
        return self.bfs(A, B)
