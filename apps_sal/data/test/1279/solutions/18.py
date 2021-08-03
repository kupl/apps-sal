[n, m] = [int(i) for i in input().split()]
a = [int(i) % 2 for i in input().split()]
b = [int(i) % 2 for i in input().split()]
print(min(sum(a), m - sum(b)) + min(sum(b), n - sum(a)))
