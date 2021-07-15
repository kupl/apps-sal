N=int(input())
p=[int(input()) for _ in range(N)]
p.sort()
print((sum(p[0:N-1])+p[-1]//2))

