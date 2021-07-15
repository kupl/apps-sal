N = int(input())
S, T = [s for s in input().split()]

ans = ""
for ss in zip(S, T):
    ans += ''.join(list(ss))

print(ans)
