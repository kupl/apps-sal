class Solution:

    def kSimilarity(self, A, B):

        def nei(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i] and x[i] != x[j]:
                    yield (x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:])
        (q, seen) = (collections.deque([(A, 0)]), {A})
        while q:
            (x, d) = q.popleft()
            print(x)
            if x == B:
                return d
            for y in nei(x):
                if y not in seen:
                    (seen.add(y), q.append((y, d + 1)))
