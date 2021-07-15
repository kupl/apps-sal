n = int(input())
s = input()
c = [0,0]
for i in range(n):
    if (s[i]=="E"):
        c[0] += 1
    else:
        c[1] += 1
b = [0,0]
ans = c[0]
for i in range(n):
    if (s[i]=="E"):
        c[0] -= 1
        b[0] += 1
    else:
        c[1] -= 1
        b[1] += 1
    ans = min(ans,c[0]+b[1])
print(ans)
