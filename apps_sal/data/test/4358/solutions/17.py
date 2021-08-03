n = int(input())
ans = 0
lis = [int(input()) for _ in range(n)]
ma = lis.pop(lis.index(max(lis)))
print(sum(lis) + int(ma * 0.5))
