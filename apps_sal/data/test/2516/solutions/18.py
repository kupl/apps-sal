N, P = map(int, input().split())
S = input()

ans = 0
if P == 2:
    for i in range(N - 1, -1, -1):
        if int(S[i]) % 2 == 0:
            ans += i + 1
elif P == 5:
    for i in range(N - 1, -1, -1):
        if int(S[i]) % 5 == 0:
            ans += i + 1
else:
    L = [0] * P
    num = 0
    for i in range(N - 1, -1, -1):
        num += int(S[i]) * pow(10, N - 1 - i, P)
        num %= P
        L[num] += 1

    ans += L[0]
    for i in range(P):
        ans += L[i] * (L[i] - 1) // 2

print(ans)
