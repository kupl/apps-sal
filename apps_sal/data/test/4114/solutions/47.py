N = int(input())

xyh = []
for i in range(N):
    xyh.append(list(map(int, input().split())))

xyh_sorted = sorted(xyh, key=lambda x: x[2], reverse=True)

answer = [0, 0, 0]
for cy in range(0, 101):
    for cx in range(0, 101):
        H = xyh_sorted[0][2] + abs(xyh_sorted[0][0] - cx) + abs(xyh_sorted[0][1] - cy)
        flag = True
        for i in range(1, N):
            h2 = max(H - abs(xyh_sorted[i][0] - cx) - abs(xyh_sorted[i][1] - cy), 0)
            if h2 != xyh_sorted[i][2]:
                flag = False
                break
        if flag:
            answer = [cx, cy, H]
            break
    if flag:
        break

answerString = str(answer[0]) + " " + str(answer[1]) + " " + str(answer[2])
print(answerString)
