n, k = map(int, input().split())
a = list(map(int, input().split()))
l = max(len(bin(k)[2:]), len(bin(max(a))[2:]))
c = [0] * l

for i in a:
    b_a = bin(i)[2:].zfill(l)
    for j in range(l):
        if b_a[j] == '1':
            c[j] += 1

x = 0
for i in range(l):
    e = l - i - 1
    if n - c[i] > c[i] and x + 2**e <= k:
        x += 2**e

ans = 0
for i in a:
    ans += i ^ x
print(ans)
