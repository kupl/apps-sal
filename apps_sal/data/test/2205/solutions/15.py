n = int(input())
p = [int(x) for x in input().split()]
d = [0 for i in range(n + 1)]
for i in range(2, n + 1):
    d[i] -= n // i
    d[n % i + 1] -= 1
    d[0] += n // i + 1
sum = 0
a = []
for i in d:
    sum += i
    a.append(sum)
ans = 0
for i in p:
    ans ^= i
for i in range(1, len(a)):
    if a[i] % 2 == 1:
        ans ^= i
print(ans)
