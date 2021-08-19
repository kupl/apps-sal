n = int(input())
l = list(map(int, input().split()))
maxx = 10000000000
cur = 0
for i in range(1, 101):
    now = 0
    for j in range(n):
        if l[j] < i:
            now += i - l[j] - 1
        elif l[j] > i:
            now += l[j] - i - 1
    if now < maxx:
        maxx = now
        cur = i
print(cur, maxx)
