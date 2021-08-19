(N, P) = map(int, input().split())
S = input()
if P == 2:
    ans = 0
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ans += i + 1
elif P == 5:
    ans = 0
    for i in range(N):
        if S[i] == '0' or S[i] == '5':
            ans += i + 1
else:
    L = [0] * P
    num = 0
    for i in range(N):
        num += int(S[N - i - 1]) * pow(10, i, P)
        num %= P
        L[num] += 1
    ans = L[0]
    for i in range(P):
        ans += L[i] * (L[i] - 1) // 2
print(ans)
