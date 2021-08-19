(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
num = -1
mino = int(1e+18)
for i in range(k):
    if mino > n % a[i]:
        num = i + 1
        mino = n % a[i]
print(num, n // a[num - 1])
