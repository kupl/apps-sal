a,b = map(int,input().split())
c = 0
for i in range(a,b+1):
    if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2]:
        c += 1
print(c)
