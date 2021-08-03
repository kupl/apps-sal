n = int(input())
k = int(input())
ans = 1
for i in range(n):
    if ans * 2 >= ans + k:
        ans = ans + k
    else:
        ans = ans * 2
print(ans)
