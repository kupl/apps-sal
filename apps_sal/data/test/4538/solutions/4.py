n,d = [int(s) for s in input().split()]
l = [[int(s) for s in input().split()] for j in range(n)]
l1 = [i[0]*i[0] + i[1]*i[1] for i in l]
l1.sort()
ans = -1
for i in range(n):
    if l1[i]>d*d:
        ans = i
        break
else:
    ans = n
print(ans)
