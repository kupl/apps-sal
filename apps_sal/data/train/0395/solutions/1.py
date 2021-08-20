class Solution:

    def oddEvenJumps(self, A: 'List[int]') -> 'int':
        sorted_indexes = sorted(list(range(len(A))), key=lambda i: A[i])
        oddnext = self.makeStack(sorted_indexes)
        sorted_indexes.sort(key=lambda i: A[i], reverse=True)
        evennext = self.makeStack(sorted_indexes)
        odd = [False] * len(A)
        even = [False] * len(A)
        odd[-1] = even[-1] = True
        for i in range(len(A) - 1, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)

    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        return result
