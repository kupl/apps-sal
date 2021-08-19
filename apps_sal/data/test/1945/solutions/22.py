n = int(input())
d = {}
for i in range(n):
    (a, b) = input().split()
    bo = True
    for j in d:
        if a == d[j]:
            d[j] = b
            bo = False
    if bo:
        d[a] = b
print(len(d))
for i in d:
    print(i, d[i])
