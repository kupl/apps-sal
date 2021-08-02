n = int(input())
a = list(map(int, input().split()))

t = 10**9
for i in range(min(a), max(a) + 1):
    num = 0
    for h in a:
        num += (h - i)**2
    if num <= t:
        t = num
print(t)
