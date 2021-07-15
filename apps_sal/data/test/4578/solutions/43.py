n,x = map(int,input().split())
m = [int(input()) for i in range(n)]
q = x-sum(m)

print(n + q//min(m))
