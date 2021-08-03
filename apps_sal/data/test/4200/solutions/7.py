n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
flag = 0
for i in range(n):
    if l[i] >= sum(l) / (4 * m):
        if n - i >= m:
            print("Yes")
        else:
            print("No")
        flag = 1
        break
if flag == 0:
    print("No")
