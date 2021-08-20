n = int(input())
a = list(map(int, input().split()))
d = a[1] - a[0]
t = 1
i = 2
while i < len(a):
    cur = a[i] - a[i - 1]
    if cur != d:
        t = 0
        break
    i = i + 1
print(a[-1] + t * d)
