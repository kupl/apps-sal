n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    print(a[i], a[-i-1])

