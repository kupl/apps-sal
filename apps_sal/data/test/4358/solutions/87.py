n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
p[n - 1] /= 2
print((int(sum(p))))
