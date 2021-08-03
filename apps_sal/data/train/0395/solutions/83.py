class Solution:
    # O(nlog(n)) Time | O(n) Space
    def oddEvenJumps(self, A: List[int]) -> int:
        nextHigher = [0] * len(A)
        nextLower = [0] * len(A)
        validOdd = [0] * len(A)
        validEven = [0] * len(A)
        validOdd[-1] = 1
        validEven[-1] = 1

        stack = []
        # sort array by value, put all smaller valunes' index in stack, if stack[-1] smaller then current index, A[stack[-a]] next higher value is at index i
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                nextLower[stack.pop()] = i
            stack.append(i)

        for index in reversed(range(len(A) - 1)):
            validOdd[index] = validEven[nextHigher[index]]
            validEven[index] = validOdd[nextLower[index]]
        return sum(validOdd)
