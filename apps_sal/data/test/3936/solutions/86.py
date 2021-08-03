N = int(input())
S1 = input()
S2 = input()

if S1[0] == S2[0]:
    ans = 3
    t = 1
else:
    ans = 6
    t = 2

for i in range(1, N):
    if S1[i] == S1[i - 1]:
        continue
    if S1[i] == S2[i]:
        if t == 1:
            ans *= 2
        t = 1
    else:
        if t == 1:
            ans *= 2
        else:
            ans *= 3
        t = 2
    ans %= 10 ** 9 + 7

print(ans)
