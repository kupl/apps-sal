(N, P) = map(int, input().split())
S = input()
ans = 0
if P == 2 or P == 5:
    for (i, s) in enumerate(S):
        if int(s) % P == 0:
            ans += i + 1
else:
    l = [0] * P
    l[0] = 1
    Sum = 0
    digits = 1
    for c in S[::-1]:
        Sum += int(c) * digits % P
        Sum %= P
        l[Sum] += 1
        digits = digits * 10 % P
    for i in range(len(l)):
        ans += l[i] * (l[i] - 1) // 2
print(ans)
