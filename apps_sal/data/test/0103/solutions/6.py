n = int(input())
n += 2
a = list(map(int, input().split()))
a = [0] + a
a = a + [1001]
ind = 0
ans = 0
while ind != n:
    now = 0
    while ind + 1 != n and a[ind] + 1 == a[ind + 1]:
        ind += 1
        now += 1
    ind += 1
    ans = max(ans, now - 1)
print(ans)
