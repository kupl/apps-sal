from collections import Counter
from copy import deepcopy


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
dp = [[0] * 26 for _ in range(N)]
if N == 1:
    print(0)
else:
    for i in range(1, N):
        dp[i] = deepcopy(dp[i - 1])
        temp = Counter(prime_factorize(i + 1))
        for x in temp.items():
            if len(prime_factorize(x[0])) == 1:
                dp[i][prime.index(x[0])] += x[1]
        four = 0
        two = 0
        fourteen = 0
        twenty_four = 0
        seventy_four = 0
        for j in range(25):
            if dp[i][j] >= 74:
                seventy_four += 1
                twenty_four += 1
                fourteen += 1
                four += 1
                two += 1
            elif dp[i][j] >= 24:
                twenty_four += 1
                fourteen += 1
                four += 1
                two += 1
            elif dp[i][j] >= 14:
                fourteen += 1
                four += 1
                two += 1
            elif dp[i][j] >= 4:
                four += 1
                two += 1
            elif dp[i][j] >= 2:
                two += 1
        dp[i][25] = ((four * (four - 1)) // 2) * (two - 2) + twenty_four * (two - 1) + fourteen * (four - 1) + seventy_four
    print(dp[N - 1][25])
