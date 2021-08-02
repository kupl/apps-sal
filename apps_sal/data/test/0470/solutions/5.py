l = list(map(int, input().split()))
mn = sum(l)
for i in range(1, 101):
    if l.count(i) >= 2:
        mn = min(mn, sum(l) - i * 2)
    if l.count(i) >= 3:
        mn = min(mn, sum(l) - i * 3)
print(mn)
