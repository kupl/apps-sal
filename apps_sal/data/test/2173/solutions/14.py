n = int(input().strip())
a = list(map(int, input().strip().split()))
t = sorted(list(range(n)), key=lambda x: a[x])
cur = -1
final = [0] * n
for elem in t:
    if cur + 1 >= a[elem]:
        cur += 1
    else:
        cur = a[elem]
    final[elem] = cur
print(' '.join((str(x) for x in final)))
'\n\n3\n5 1 1\n\n1\n1000000\n\n'
