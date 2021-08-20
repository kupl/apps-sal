N = int(input())


def cd(n):
    ls = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            ls += [i, n // i]
    return ls


ans = len(set(cd(N - 1))) - 1
for j in set(cd(N)):
    a = N
    if not j == 1:
        while a % j == 0:
            a //= j
        if a % j == 1:
            ans += 1
print(ans)
