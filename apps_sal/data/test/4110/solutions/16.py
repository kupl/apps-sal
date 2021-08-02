# 未知のアルゴリズムか天才系DPかと思ってすぐ諦めて解説読んでしまった

d, g = list(map(int, input().split()))
points = []
for _ in range(d):
    p, c = list(map(int, input().split()))
    points.append((p, c))
ans = 10**12
for bit in range(2**d):
    arr = [False] * d
    for i in range(d):
        if bit >> i & 1 == 1:
            arr[i] = True
    tmp_sum = 0
    count = 0
    for i in range(d):
        if arr[i]:
            # kompuli-to
            tmp_sum += points[i][1]
            tmp_sum += (i + 1) * 100 * points[i][0]
            count += points[i][0]
    if tmp_sum < g:
        # 達成できるまで得点の高いやつからやっていく
        for i in range(d - 1, -1, -1):
            if arr[i]:
                # すでにkompuli-toしてるので
                continue
            used = 0
            for j in range(points[i][0]):
                if tmp_sum < g:
                    tmp_sum += (i + 1) * 100
                    count += 1
                    used += 1
            if used == points[i][0]:
                tmp_sum += points[i][1]
            if tmp_sum >= g:
                break
    ans = min(ans, count)
print(ans)
