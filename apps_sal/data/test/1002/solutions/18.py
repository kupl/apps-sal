n,d=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
print(-1) if sum(t)+(len(t)-1)*10>d else print((d-sum(t))//5)
