n = input()
k = int(input())
MOD = int(1000000000.0 + 7)
a = {0: 0, 1: 0, 2: 1}
for i in range(3, 1001):
    s = bin(i)[2:]
    ones_count = 0
    for x in s:
        if x == '1':
            ones_count += 1
    a[i] = a[ones_count] + 1
answer = 0
table = {}


def bin_coeff(N, K):
    if K > N:
        raise Exception
    if K > N // 2:
        K = N - K
    if K == 0:
        table[N, 0] = 1
        return 1
    if (N, K) not in table:
        table[N, K] = N * bin_coeff(N - 1, K - 1) // K
    return table[N, K]


ones = 0
for (i, x) in enumerate(n):
    if x == '1':
        good = []
        N = len(n) - i - 1
        min = 0 if i > 0 else 1
        for j in range(min, N + 1):
            if a[j + ones] == k - 1:
                good.append(j)
        for x in good:
            answer = (answer + bin_coeff(N, x)) % MOD
            if i == 0 and x == 1:
                answer -= 1
        ones += 1
if a[ones] == k - 1:
    answer += 1
if k == 0:
    answer = 1
if k == 1:
    answer = len(n) - 1
answer = int(answer)
print(answer)
