N = input()
K = int(input())
ans = '1'
for i in range(K):
    if i >= len(N):
        break
    if N[i] != '1':
        ans = N[i]
        break
print(ans)
