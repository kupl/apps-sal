S = input()


def f(x):
    return 2 ** (x - 1) if x > 0 else 1


lenS = len(S)
ans = 0
for i in range(1, lenS + 1):
    for j in range(lenS - i + 1):
        ans += int(S[j:j + i]) * f(j) * f(lenS - j - i)
print(ans)
