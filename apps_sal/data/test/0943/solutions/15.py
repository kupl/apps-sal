n = int(input())
a = [int(i) for i in input().split()]
if not sum(a) % 2:
    print(sum(a))
    return
a.sort()
ans = 0
flag = True
for i in range(n):
    if (flag and (not (a[i] % 2))) or (not flag):
        ans += a[i]
    else:
        flag = False
print(ans)


