import heapq
n = int(input())
inf = 10000000000000
# 始まりと終わりを保持
# 同じオブジェクトにするやつで一時間溶かした、しね
ans = [[-1, -1] for i in range(n)]
ans[-1][1] = 0
ans[0][0] = 0
t = list(map(int, input().split()))
v = list(map(int, input().split()))
v2 = []
for i in range(n):
    heapq.heappush(v2, (v[i], i))
for i in range(n):
    # print(ans)
    y = heapq.heappop(v2)
    # print(y[1])
    # print(ans[y[1]])
    # print(y)
    # 始まりをまずは決める
    if ans[y[1]][0] == -1:
        # print(2)
        now1 = 0
        ansi1 = inf
        for j in range(y[1] - 1, -1, -1):
            # print(ans1)
            if ans[j][1] != -1:
                ansi1 = min(ansi1, ans[j][1] + now1)
            now1 += t[j]
            if ans[j][0] != -1:
                ansi1 = min(ansi1, ans[j][0] + now1)
        now1 = 0
        for j in range(y[1], n):
            if ans[j][0] != -1:
                ansi1 = min(ansi1, ans[j][0] + now1)
            now1 += t[j]
            if ans[j][1] != -1:
                ansi1 = min(ansi1, ans[j][1] + now1)
        ans[y[1]][0] = min(ansi1, y[0])
        ans[y[1] - 1][1] = ans[y[1]][0]
        # print(ansi1)
    if ans[y[1]][1] == -1:
        # print(3)
        now2 = 0
        ansi2 = inf
        for j in range(y[1], -1, -1):
            if ans[j][1] != -1:
                ansi2 = min(ansi2, ans[j][1] + now2)
            now2 += t[j]
            if ans[j][0] != -1:
                ansi2 = min(ansi2, ans[j][0] + now2)
        now2 = 0
        for j in range(y[1] + 1, n):
            if ans[j][0] != -1:
                ansi2 = min(ansi2, ans[j][0] + now2)
            now2 += t[j]
            if ans[j][1] != -1:
                ansi2 = min(ansi2, ans[j][1] + now2)
        ans[y[1]][1] = min(ansi2, y[0])
        ans[y[1] + 1][0] = ans[y[1]][1]
        # print(ansi2)
answer = 0
for i in range(n):
    h = min((t[i] + sum(ans[i])) / 2, v[i])
    answer += ((h**2 - ans[i][0]**2) / 2)
    answer += ((h**2 - ans[i][1]**2) / 2)
    answer += (h * (t[i] + sum(ans[i]) - 2 * h))
print(answer)
# print(ans)
