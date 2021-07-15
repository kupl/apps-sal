n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(min([max([a[j] * b[k] for j in range(n) for k in range(m) if i != j]) for i in range(n)]))

