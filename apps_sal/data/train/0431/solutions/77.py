class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        stack = []
        my_dict = {}
        for i in range(0, len(A)):
            if stack == []:
                stack.append((i, A[i]))
                my_dict[i, A[i]] = [0]
            elif A[i] >= stack[-1][1]:
                stack.append((i, A[i]))
                my_dict[i, A[i]] = [0]
            else:
                while stack != [] and A[i] < stack[-1][1]:
                    temp = stack.pop()
                    my_dict[temp].append(i - temp[0] - 1)
                if stack == []:
                    stack.append((i, A[i]))
                    my_dict[i, A[i]] = [i]
                else:
                    stack.append((i, A[i]))
                    my_dict[i, A[i]] = [i - 1 - stack[-2][0]]
        for key in my_dict:
            if len(my_dict[key]) == 1:
                my_dict[key].append(len(A) - 1 - key[0])
            result += key[1] * (my_dict[key][0] + 1) * (my_dict[key][1] + 1)
        return result % MOD
