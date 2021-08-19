N = int(input())
W = [input() for i in range(N)]
ans = 'Yes'
last = ''
for i in range(N):
    for j in range(i):
        if W[i] == W[j]:
            ans = 'No'
for w in W:
    W_new = [i for i in w]
    if w != W[0] and last != W_new[0]:
        ans = 'No'
    last = W_new[-1]
print(ans)
