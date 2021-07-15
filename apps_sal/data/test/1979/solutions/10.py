n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
p = [0] * n
q = [0] * n
for i in range(n):
    p[a[i] - 1] = i
    q[b[i] - 1] = i
for i in range(n):
    c[(p[i] - q[i]) % n] += 1
print(max(c))
