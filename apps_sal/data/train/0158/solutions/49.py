from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        if A == B:
            return 0

        queue = deque([])
        queue.append(A)
        step = 0
        visited = set()
        while queue:
            length = len(queue)

            while length:
                length -= 1
                strings = queue.popleft()

                i = 0
                while strings[i] == B[i]:
                    i += 1
                newstrings = list(strings)
                cha = strings[i]
                for j in range(i + 1, len(strings)):
                    if strings[j] == B[i] and strings[j] != B[j]:
                        newstrings[i], newstrings[j] = newstrings[j], newstrings[i]
                        newstrings = ''.join(newstrings)
                        if newstrings == B:
                            return step + 1
                        else:
                            if newstrings not in visited:
                                visited.add(newstrings)
                                queue.append(newstrings)
                        newstrings = list(strings)

            step += 1
