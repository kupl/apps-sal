n = int(input())
a = list(input())
f = list(map(int, input().split()))
f = {i + 1: f[i] for i in range(9)}
st = n
for i in range(n):
    c = int(a[i])
    if f[c] > c:
        st = i
        break
for i in range(st, n):
    c = int(a[i])
    if f[c] >= c:
        a[i] = str(f[c])
    else:
        break
print(''.join(a))
