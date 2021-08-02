n, q = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
arr.sort(reverse=True)
b = [0] * (n + 2)
z = [0] * (n + 2);
s = 0
for x in range(q):
    l, r = list(map(int, input().strip().split()))
    b[l] += 1
    b[r + 1] -= 1
# print(b)
for x in range(1, n + 1):
    z[x] = z[x - 1] + b[x]
# print(z)
z.sort(reverse=True)
for x in range(n):
    s += z[x] * arr[x]
print(s)
