K = int(input())
N = 50
div_K, rem_K = divmod(K, N)
ans = [l + div_K for l in range(N)]
for i in range(rem_K):
    idx = ans.index(min(ans))
    for i in range(N):
        if i == idx:
            ans[i] += N
        else:
            ans[i] -= 1
print(N)
print((*ans))

