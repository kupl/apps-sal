n = int(input())
a = sorted(map(int , input().split()))
ans = 0
for i in range(n):
    f = 1
    for j in range(i):
        if a[i] % a[j] == 0:
            f = 0
            break
    ans += f
print(ans)
