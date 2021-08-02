n = int(input())
b = set()
a = [int(s) for s in input().split()]
res = 0
for i in a:
    if not i in b:
        b.add(i)
    else:
        while True:
            res += 1
            i += 1
            if not i in b:
                b.add(i)
                break
print(res)
