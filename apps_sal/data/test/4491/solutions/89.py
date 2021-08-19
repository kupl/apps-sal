n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
acount = 0
bcount = 0
ans = 0
for i in range(n):
    bcount = 0
    acount += a[i]
    for j in range(i, n):
        bcount += b[j]
        if ans < acount + bcount:
            ans = acount + bcount
print(ans)
