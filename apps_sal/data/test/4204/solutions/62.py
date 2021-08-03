S = input()
N = len(S)
K = int(input())

if S[:min(N, K)] == "1" * min(N, K):
    ans = 1
else:
    for i in range(N):
        if S[i] != "1":
            ans = S[i]
            break

print(ans)
