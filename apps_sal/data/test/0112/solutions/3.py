def f(m):
    m = list(map(int, list(str(m))))
    #print(m)
    for k in range(dd[n]):
        #print(d[k])
        cur = 0
        for j in range(n):
            kub = d[k][j] - 1
            if cur == len(m):
                return True
            if m[cur] in a[kub]:
                cur += 1
        if cur == len(m):
            return True
    return False
                

n = int(input())
a = [[], [], []]
for i in range(n):
    a[i] = list(map(int, input().split()))
d = [[1, 2, 3], [2, 1, 3], [1, 3, 2], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
dd = [0, 0, 2, 6]
if n == 1:
    for j in range(1, 10):
        if j not in a[0]:
            print(j - 1)
            return
ans = 0
while f(ans + 1):
    ans += 1
#print(f(88))
print(ans)

