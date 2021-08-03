s = list(input()) + ["A"]
ans = 1
k = 0
l = ['A', 'E', 'I', 'O', 'U', 'Y']
for x in s:
    k += 1
    if ans < k:
        ans = k
    if x in l:
        k = 0
print(ans)
