n = int(input())
a = [int(x) for x in input().split()]
(x, f) = [int(x) for x in input().split()]
res = 0
for i in a:
    if i > x:
        res += f * int(i / (f + x))
        if i % (f + x) > x:
            res += f
print(res)
