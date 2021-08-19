MOD = 10 ** 9 + 7
N = int(input())
S1 = input()
S2 = input()
l = []
res = 1
while res < N:
    if S1[res - 1] == S1[res]:
        l.append(2)
        res += 2
    else:
        l.append(1)
        res += 1
if res == N:
    l.append(1)
n = len(l)
if l[0] == 1:
    ans = 3
else:
    ans = 6
for i in range(1, n):
    if l[i] == 1 and l[i - 1] == 1:
        ans = ans * 2 % MOD
    elif l[i] == 2 and l[i - 1] == 1:
        ans = ans * 2 % MOD
    elif l[i] == 2 and l[i - 1] == 2:
        ans = ans * 3 % MOD
print(ans)
