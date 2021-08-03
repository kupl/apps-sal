n = int(input())
red, blue = [], []
for _ in range(n):
    a, b = list(map(int, input().split()))
    red.append([a, b, min(a, b)])
for _ in range(n):
    a, b = list(map(int, input().split()))
    blue.append([a, b, min(a, b)])

red.sort(key=lambda x: x[1])
blue.sort(key=lambda x: x[0])
status = [False for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n - 1, -1, -1):
        if not status[j]:
            if red[j][0] < blue[i][0] and red[j][1] < blue[i][1]:
                ans += 1
                status[j] = True
                break
print(ans)
