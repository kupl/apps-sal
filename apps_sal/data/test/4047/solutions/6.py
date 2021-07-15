n = int(input())
a = list(map(int, input().split()))
c1 = 0
c2 = 0
for i in range(n):
    if a[i] % 2 == 0:
        c1 += 1
    else:
        c2 += 1
print(min(c1, c2))

