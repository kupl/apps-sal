class Solution:
    # save the indices of letters that are in the right place
    # create array 'correct' where the index corresponds to the letter in A and the value is the correct index
    # find every letter pair --> a pair is two letters in B that when swapped, will end up in the correct index
    # dynamic programming? number of displaced letters --> min # of swaps
    # subproblem = number of displaced letters
    # at most 20 swaps
    def kSimilarity(self, A: str, B: str) -> int:
        q, visited = [(A, 0)], {A}
        # BFS
        for x, dist in q:
            if x == B:
                return dist
            for y in self.generate_neighbour_strings(x, B):
                if y not in visited:
                    visited.add(y), q.append((y, dist + 1))

    def generate_neighbour_strings(self, x, B):
        i = 0
        while x[i] == B[i]:
            i += 1
        for j in range(i + 1, len(x)):
            if x[j] == B[i] and x[j] != B[j]:
                yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
