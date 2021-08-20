def fac(n):
    b = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.append(i)
            if i != n // i:
                b.append(n // i)
    return b


n = int(input())
a = list(map(int, input().split()))
s = sum(a)
m = 10 ** 9
a.sort()
for i in a[::-1]:
    for j in fac(i):
        m = min(m, s + a[0] * j + i // j - a[0] - i)
print(m)
