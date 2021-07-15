l = []
ans = 0
for i in range(5):
    x = int(input())
    ans +=x
    if x%10 == 0:
        l.append(0)
    else:
        l.append(10-x%10)
l.sort()
ans +=  sum(l[:4])
print(ans)
