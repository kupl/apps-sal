n = int(input())
a = list(map(int, input().split(" ")))

v = 0

for i in range(n):
    v += a[i]
    if (v - i) % 2 == 0:
        print(1)
    else:
        print(2)
