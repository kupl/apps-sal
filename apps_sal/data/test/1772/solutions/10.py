n = int(input())
a = list(map(int, input().split()))
q = [0] * 2
for i in range(n):
    q[a[i] % 2] += 1
x = min(q[0], q[1])
q[0] -= x
q[1] -= x
print(x + q[1] // 3)
