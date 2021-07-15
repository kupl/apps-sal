n,x = map(int,input().split())
m =[]
for _ in range(n):
    m.append(int(input()))
print((x - sum(m))//min(m)+n)
