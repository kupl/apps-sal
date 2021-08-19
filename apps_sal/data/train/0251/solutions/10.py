class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return N
        i = N - 1
        operations = []
        curr = N
        which_op = 0
        while i >= 1:

            if which_op == 0:
                curr *= i
                curr = int(curr)
                which_op += 1
            elif which_op == 1:
                curr /= i
                curr = int(curr)
                which_op += 1
            elif which_op == 2:
                operations.append((curr, 2))
                curr = i
                which_op += 1
            elif which_op == 3:
                operations.append((curr, 3))
                which_op = 0
                curr = i
                which_op = 0
            if i == 1:
                operations.append((curr, 0))
            i -= 1

        # print(operations)
        sol = 0
        index = 0
        if len(operations) == 1:
            return operations[0][0]
        while index < len(operations) - 1:
            if index == 0:
                sol = operations[index][0]

            if operations[index][1] == 2:
                sol += operations[index + 1][0]
            else:
                sol -= operations[index + 1][0]
            index += 1
        return sol
