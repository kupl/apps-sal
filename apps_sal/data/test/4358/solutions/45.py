n = int(input())
p = [int(input()) for i in range(n)]
print(max(p) // 2 + sum(p) - max(p))
