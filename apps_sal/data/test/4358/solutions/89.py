n=int(input())

p=[int(input()) for i in range(n)]

ans=max(p)//2+sum(p)-max(p)

print(ans)
