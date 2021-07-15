N = int(input())
S, T = input().split()

ans = ""
for i in range(0, N):
    ans = ans + S[i] + T[i]
print(ans)
