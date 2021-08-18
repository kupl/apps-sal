class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        dic = {c: i for i, c in enumerate('abcdef')}

        bag = dict()

        stack = []

        for a, b in zip(A, B):
            if a != b:
                i, j = dic[a], dic[b]
                bag[(i, j)] = bag.get((i, j), 0) + 1
                stack.append((i, j))

        output = 0

        def search(stack):
            if not stack:
                return 0

            i, j = stack.pop()

            if (j, i) in stack:
                idx = stack.index((j, i))
                stack = stack[:idx] + stack[(idx + 1):]

                return search(stack) + 1

            else:

                best = float(inf)

                for idx, pair in enumerate(stack):

                    if pair[0] == j:

                        curr = search(stack[:idx] + [(i, pair[1])] + stack[(idx + 1):]) + 1

                        best = min(curr, best)

                return best

        return search(stack)
