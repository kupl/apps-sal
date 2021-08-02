n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = list(set(a))
num = 0
for i in b:
    for t in b:
        if i != t:
            num += a.count(i) * a.count(t)
print(num // 2)
