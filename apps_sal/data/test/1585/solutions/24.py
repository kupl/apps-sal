x,y = map(int,input().split())
ans = x
j = 0
while ans <= y:
    ans *= 2
    j += 1
print(j)
