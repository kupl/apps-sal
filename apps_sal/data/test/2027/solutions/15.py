n = int(input())
v = [int(i) for i in input().split()]
b = [v[i] + v[i + 1] for i in range(n - 1)]
b.append(v[-1])
for i in range(n):
    print(b[i], end=" ")
