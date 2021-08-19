n = int(input())
a = list((int(x) for x in input().split()))
count = 0
z = True
j = 0
if 1 not in a:
    print(-1)
else:
    for k in range(j, n):
        if a[k] == count + 1:
            j = k
            count = count + 1
    print(n - count)
