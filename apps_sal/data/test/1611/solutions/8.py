3
n = int(input())
v = list(map(int, input().split()))
M = max(v)
v.remove(M)
print(M - sum(v) + 1)
