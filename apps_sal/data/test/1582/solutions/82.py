N = int(input())
l = [[0] * 10 for i in range(10)]

for i in range(1, N+1):
    s = len(str(i))
    if s == 1:
        l[i][i] += 1
    else:
        l[i//(10**(s-1))][i%10] += 1

ans = 0

for i in range(1, 10):
    for j in range(1, 10):
        ans += l[i][j] * l[j][i]

#for i in range(10):
#    print(l[i])

print(ans)
