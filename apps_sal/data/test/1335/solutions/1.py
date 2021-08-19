(n, k) = list(map(int, input().split()))
lst = list(map(int, input().split()))
cur = []
if n < k:
    k = n
for i in range(k):
    cur.append([1, lst[i]])
t = 0
ans = 0
m = 0
used = [False] * k
while m != n:
    t += 1
    for i in range(len(cur)):
        cur[i][0] += 1
        if cur[i][0] == cur[i][1] + 1 and cur[i][1] != -1:
            m += 1
            used[i] = False
            if k != n:
                cur[i] = [1, lst[k]]
                k += 1
            else:
                cur[i] = [0, -1]
                used[i] = True
    x = 100 * m / n
    if x % 1 >= 0.5:
        x = x // 1 + 1
    else:
        x //= 1
    x = int(x)
    for i in range(len(cur)):
        if cur[i][0] == x and (not used[i]):
            used[i] = True
            ans += 1
print(ans)
