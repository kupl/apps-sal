def GetDiv(n):
    Div = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            Div.append(i)
            Div.append(n // i)
        i += 1
    return sorted(list(set(Div)))


N = int(input())
Ans = []
Ans.append(N * (N + 1) // 2)
for i in GetDiv(N):
    M = N // i
    Ans.append(M * (1 - i) + i * M * (M + 1) // 2)
print(' '.join(map(str, sorted(list(set(Ans))))))
