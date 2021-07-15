n = int(input())
l = [int(input()) for i in range(n)]

ans = sum(l) - max(l) + max(l)//2
print(ans)
