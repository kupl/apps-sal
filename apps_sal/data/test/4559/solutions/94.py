n = int(input())
l = list(map(int, input().split()))
ans = 1
if 0 in l:
    ans = 0
else:
    for i in range(n):
        ans = ans * l[i]
        if ans > 10 ** 18:
            ans = -1
            break
print(ans)
