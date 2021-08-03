n = int(input())
d = [int(x) for x in input().split()]
print((sum(d[i] * d[j] for i in range(n) for j in range(i + 1, n))))
