n = int(input())

lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

F = False
for x in range(4):
    ans = [-1] * n
    ans[0] = x
    for y in range(1, n):
        f = False
        for z in range(4):
            if z | ans[y - 1] == lst1[y - 1] and z & ans[y - 1] == lst2[y - 1]:
                ans[y] = z
                f = True
                break
        if not f:
            break

    if f:
        F = True
        break

if F:
    print("YES")
    print(*ans)
else:
    print("NO")
