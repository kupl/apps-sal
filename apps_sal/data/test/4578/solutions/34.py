(N, X) = map(int, input().split())
m = [int(input()) for i in range(N)]
m.sort()
nokori = X - sum(m)
Nokori = nokori // m[0]
print(Nokori + N)
