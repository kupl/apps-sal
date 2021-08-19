n = int(input())
w = []
ans = 'Yes'
for i in range(n):
    w.append(input())
if len(set(w)) < len(w):
    ans = 'No'
for i in range(1, n):
    if w[i][0] != w[i - 1][-1]:
        ans = 'No'
print(ans)
