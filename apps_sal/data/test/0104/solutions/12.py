n = int(input())
a = [int(i) for i in input().split()]
s = sum(a)
ss = 0
for i in range(n):
    ss += a[i]
    if (ss * 2 >= s):
        print(i + 1)
        break

