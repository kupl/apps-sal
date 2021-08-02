n = int(input())
a = [int(i) for i in input().split()]
c = 0
for i in range(n):
    if a[i] > c:
        print(i + 1)
        break
    else:
        c = max(a[i] + 1, c)
else:
    print(-1)
