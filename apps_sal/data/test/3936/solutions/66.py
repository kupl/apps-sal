import sys

input = sys.stdin.readline
N = int(input())
S1 = input().strip()
S2 = input().strip()

mod = 10**9 + 7
ans = 1
prev = ""
for i in range(N):
    if i == 0:
        ans *= 3
        if S1[i] != S2[i]:
            ans *= 2
    else:
        if S1[i - 1] == S1[i]:
            pass
        else:
            if S1[i - 1] == S2[i - 1]:
                ans *= 2
                ans %= mod
            else:
                if S1[i] == S2[i]:
                    pass
                else:
                    ans *= 3
                    ans %= mod

print(ans)
