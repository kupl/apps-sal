class Solution:
    def previousLessNumber(self, A: List[int]) -> List[int]:
        plmStack = []
        plmResult = [-1] * len(A)
        i = 0
        while (i < len(A)):
            while(len(plmStack) > 0 and A[plmStack[-1]] >= A[i]):
                plmStack.pop()
            plmResult[i] = -1 if len(plmStack) == 0 else plmStack[-1]
            plmStack.append(i)
            i += 1
        return plmResult

    def nextLessNumber(self, A: List[int]) -> List[int]:
        nlmStack = []
        nlmResult = [-1] * len(A)
        i = len(A) - 1
        while (i >= 0):
            while(len(nlmStack) > 0 and A[nlmStack[-1]] > A[i]):
                nlmStack.pop()
            nlmResult[i] = -1 if len(nlmStack) == 0 else nlmStack[-1]
            nlmStack.append(i)
            i -= 1
        return nlmResult

    def sumSubarrayMins(self, A: List[int]) -> int:
        plmResult = self.previousLessNumber(A)
        nlmResult = self.nextLessNumber(A)
        print(plmResult)
        print(nlmResult)
        sum = 0
        for i in range(len(A)):
            leftDist = 0
            if plmResult[i] == -1:
                leftDist = i + 1
            else:
                leftDist = i - plmResult[i]

            rightDist = 0
            if nlmResult[i] == -1:
                rightDist = len(A) - i
            else:
                rightDist = nlmResult[i] - i

            sum = (sum + (A[i] * leftDist * rightDist)) % (10**9 + 7)
        return sum
