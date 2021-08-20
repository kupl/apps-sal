n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
total = 0
c = 0
for i in a:
    if total <= i:
        c += 1
        total += i
print(c)
