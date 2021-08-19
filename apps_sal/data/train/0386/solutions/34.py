def countVowels(x, n, memo):
    convert = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    x_val = convert[x]
    if n == 1:
        return 1
    if memo[x_val][n] != -1:
        return memo[x_val][n]
    if x == 'a':
        memo[x_val][n] = countVowels('e', n - 1, memo)
        return memo[x_val][n]
    elif x == 'u':
        memo[x_val][n] = countVowels('a', n - 1, memo)
        return memo[x_val][n]
    elif x == 'e':
        memo[x_val][n] = countVowels('a', n - 1, memo) + countVowels('i', n - 1, memo)
        return memo[x_val][n]
    elif x == 'o':
        memo[x_val][n] = countVowels('i', n - 1, memo) + countVowels('u', n - 1, memo)
        return memo[x_val][n]
    elif x == 'i':
        memo[x_val][n] = countVowels('a', n - 1, memo) + countVowels('e', n - 1, memo) + countVowels('o', n - 1, memo) + countVowels('u', n - 1, memo)
        return memo[x_val][n]


class Solution:

    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        else:
            memo = [[-1 for j in range(n + 1)] for i in range(5)]
            res = countVowels('a', n, memo) + countVowels('e', n, memo) + countVowels('i', n, memo) + countVowels('o', n, memo) + countVowels('u', n, memo)
            return res % 1000000007
