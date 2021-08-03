def get_nsge_ngse(a):
    ngse_stack = []
    nsge_stack = []
    ngse = [-1] * len(a)
    nsge = [-1] * len(a)
    for i, item in sorted(enumerate(a), key=lambda x: (x[1], x[0])):
        while nsge_stack and i > nsge_stack[-1]:
            nsge[nsge_stack.pop()] = i
        nsge_stack.append(i)
    for i, item in sorted(enumerate(a), key=lambda x: (-1 * x[1], x[0])):
        while ngse_stack and i > ngse_stack[-1]:
            ngse[ngse_stack.pop()] = i
        ngse_stack.append(i)
    return(nsge, ngse)


def get_ways(a):
    odd, even = get_nsge_ngse(a)
    print(odd, even)
    dp = [set() for x in a]
    dp[-1].add('even')
    dp[-1].add('odd')
    count = 1
    for i in range(len(a) - 2, -1, -1):
        if odd[i] != -1 and 'even' in dp[odd[i]]:
            dp[i].add('odd')
        if even[i] != -1 and 'odd' in dp[even[i]]:
            dp[i].add('even')
        if 'odd' in dp[i]:
            count += 1
    return count


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        return get_ways(A)
