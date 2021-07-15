N = int(input())

reds = []
for i in range(N):
    a, b = list(map(int, input().split()))
    reds.append([a,b])
reds.sort(key=lambda x: x[1], reverse=True)

blues = []
for i in range(N):
    c, d = list(map(int, input().split()))
    blues.append([c,d])
blues.sort()

flag = [False for i in range(N)]
ans = 0
for i in range(N):
    c, d = blues[i][0], blues[i][1]
    for j in range(N):
        if flag[j] == True:
            continue
        a, b = reds[j][0], reds[j][1]
        if c>a and d>b:
            flag[j] = True
            ans += 1
            break
print(ans)

