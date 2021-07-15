n = int(input())
l = [0]*101
i = 2
for i in range(2,n+1):
    j = 2
    while i >= 2:
        while i % j == 0:
            i = i//j
            l[j] += 1
        j += 1

ans = sum(x >= 74 for x in l)

a = sum(x >= 2 for x in l)
b = sum(x >= 24 for x in l)
ans += b*(a-1)

a = sum(x >= 4 for x in l)
b = sum(x >= 14 for x in l)
ans += b*(a-1)

a = sum(x >= 2 for x in l)
b = sum(x >= 4 for x in l)
ans += b*(b-1)*(a-2)//2

print(ans)
