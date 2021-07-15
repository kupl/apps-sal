N = int(input())
P = list(int(input()) for i in range(N))
expensive = max(P)
other = sum(P) - expensive

print(expensive // 2 + other)
