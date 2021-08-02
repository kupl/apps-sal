n = int(input())
a = list(map(int, input().split()))
b = [1]
for i in range(1, n):
    if(a[i] == a[i - 1]):
        b[-1] += 1
    else:
        b.append(1)
m = 0
for i in range(1, len(b)):
    if(min(b[i], b[i - 1]) > m):
        m = min(b[i], b[i - 1])
print(2 * m)
