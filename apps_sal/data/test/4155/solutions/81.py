n = int(input())
h = list(map(int, input().split()))
cnt = 0
status = False
for i in range(100):
    for j in range(n):
        if h[j] > 0 and status == True:
            h[j] -= 1
        elif h[j] > 0:
            cnt += 1
            h[j] -= 1
            status = True
        else:
            status = False

        if j == n - 1:
            status = False
print(cnt)
