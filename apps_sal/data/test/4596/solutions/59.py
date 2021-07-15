n = int(input())
aa = list(map(int, input().split()))
ans = 100
for i in range(n):
    x = 0
    while aa[i] > 0:
        if aa[i] % 2 != 0:
            break
        aa[i] //= 2
        x += 1
    ans = min(ans, x)
print(ans)

