n, x = list(map(int, input().split()))

m = [int(input()) for _ in range(n)]

m.sort()

print(n + ((x - sum(m)) // m[0]))
