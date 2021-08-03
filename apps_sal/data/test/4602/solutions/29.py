a = int(input())
b = int(input())
c = list(map(int, input().split()))
total = 0
for i in range(a):
    d = 2 * c[i]
    e = 2 * abs(b - c[i])
    total += min(d, e)
print(total)
