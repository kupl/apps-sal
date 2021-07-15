n = int(input())
P = [[float(x) for x in input().split()] for _ in range(n)]
print(5 + sum(b for a,b in P)/n)

