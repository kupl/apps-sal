def count_one(n):
    c = 0
    while n:
        n = n & n - 1
        c = c + 1
    return c


nmk = input()
b = nmk.split(' ')
n = int(b[0])
m = int(b[1])
k = int(b[2])
a = []
for i in range(m + 1):
    istr = input()
    a.append(int(istr))
ans = 0
for i in range(m):
    if count_one(a[i] ^ a[m]) <= k:
        ans = ans + 1
print(ans)
