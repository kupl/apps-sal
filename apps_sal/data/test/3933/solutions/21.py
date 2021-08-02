n = int(input())
a = list(map(int, input().split()))
diff = abs(a[0] - a[1])
flag = True
for i in range(2, n):
    if abs(a[i] - a[i - 1]) != diff:
        flag = False
        break
if flag:
    if a[n - 2] >= a[n - 1]:
        print(a[n - 1] - diff)
    else:
        print(a[n - 1] + diff)
else:
    print(a[n - 1])
