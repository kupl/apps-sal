def li():
    return list(map(int, input().split()))
n, m = li()
a = li()
aa = [0] * n
for b in a:
    aa[b - 1] += 1
print(min(aa))

