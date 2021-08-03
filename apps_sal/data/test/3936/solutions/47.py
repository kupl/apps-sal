N = int(input())
S_1 = input()
S_2 = input()
MOD = 10**9 + 7

if N == 1:
    print(3)
    return

ans = 3 if S_1[0] == S_2[0] else 6

for i in range(1, N):
    if S_1[i - 1] == S_1[i]:
        continue
    if S_1[i - 1] == S_2[i - 1]:
        ans = ans * 2 % MOD
    elif S_1[i] != S_2[i]:
        ans = ans * 3 % MOD
print(ans)
