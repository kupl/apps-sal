n = int(input())
a = list(map(int, input().split()))
c = [0] * (10**5 + 3)
for i in range(n):
    c[a[i]] += 1
    c[a[i] - 1] += 1
    c[a[i] + 1] += 1
print(max(c))
