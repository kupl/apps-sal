n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
p[len(p) - 1] = p[len(p) - 1] // 2
print(sum(p))
