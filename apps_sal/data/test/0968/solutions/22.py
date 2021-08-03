n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i] = input().split()
d = list(map(int, input().split()))


answer = "YES"
c[0] = min(a[d[0] - 1], b[d[0] - 1])
for i in range(1, n):
    if c[i - 1] < min(a[d[i] - 1], b[d[i] - 1]):
        c[i] = min(a[d[i] - 1], b[d[i] - 1])
    elif c[i - 1] < max(a[d[i] - 1], b[d[i] - 1]):
        c[i] = max(a[d[i] - 1], b[d[i] - 1])
    else:
        answer = "NO"
        break
print(answer)
