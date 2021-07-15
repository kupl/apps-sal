N = int(input())
p = list(int(input()) for _ in range(N))

print(sum(p) - max(p) // 2)
