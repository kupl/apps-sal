n = int(input())
a = list(map(int, input().split()))
b = []
c = []
for k in a:
    if k > 0:
        b.append(k)
    else:
        c.append(k)
print(sum(b) - sum(c))
