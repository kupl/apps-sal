class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def dist(a, b):
            return sum((1 if c != d else 0 for (c, d) in zip(a, b)))

        def swap(s, i, j):
            if i > j:
                i, j = j, i
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        def DFS(string, k, seen):
            if string in seen:
                return False, 0
            seen.add(string)
            if string == A:
                return True, 1

            distance = dist(string, A)
            best = distance / 2 if distance % 2 == 0 else (distance // 2) + 1
            if k < best:
                return False, 1

            neighbors = []
            for i, c in enumerate(string):
                if A[i] == c:
                    continue
                for j in range(i + 1, len(A)):
                    if string[j] == A[i] and A[j] != A[i]:
                        double_play = string[i] == A[j]
                        change = -2 if double_play else -1
                        if k == best and distance % 2 == 1 and distance > 3 and not double_play:
                            continue
                        neighbor = swap(string, i, j)
                        neighbors.append((change, neighbor))
            neighbors.sort()

            total_count = 1
            for (score, neighbor) in neighbors:
                found, count = DFS(neighbor, k - 1, seen)
                total_count += count
                if found:
                    return True, total_count

            return False, total_count

        for k in range(len(A), -1, -1):
            found, count = DFS(B, k, set())
            if not found:
                return k + 1
        return 0
