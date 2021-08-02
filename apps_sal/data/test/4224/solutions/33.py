n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(29, 0, -1):
        if a[i] % (2 ** j) == 0:
            ans += j
            break
print(ans)
