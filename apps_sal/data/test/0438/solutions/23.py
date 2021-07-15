n = int(input())
c=1
sol = []
while n>c:
    n = n-c
    sol.append(c)
    c=c+1
if n >= c:
    sol.append(n)
else:
    sol[-1] += n
print(len(sol))
print(*sol)

