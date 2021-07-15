import heapq


t = int(input())
for _ in range(t):
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n)]
    info = sorted(info)
    cnt = [0] * n
    for i in range(n):
        ind = info[i][0]
        cnt[ind] += 1
    ruiseki_cnt = [0] * (n+1)
    for i in range(n):
        ruiseki_cnt[i+1] = ruiseki_cnt[i] + cnt[i]
    # print(cnt)
    # print(ruiseki_cnt)
    need = [0] * n
    for i in range(1,n):
        if cnt[i] != 0 and i > ruiseki_cnt[i]:
            need[i] = min(i - ruiseki_cnt[i], i)
    # print(need)
    info = sorted(info, reverse = True)
    #print(info)

    num = n - 1
    pos = 0
    q = []
    used_cnt = 0
    ans = 0
    while True:
        if num == -1:
            break
        while True:
            if pos < n and info[pos][0] >= num:
                heapq.heappush(q, info[pos][1])
                pos += 1
            else:
                break
        if need[num] - used_cnt > 0:
            tmp = need[num] - used_cnt
            for _ in range(tmp):
                ans += heapq.heappop(q)
            used_cnt += tmp
        num -= 1
    print(ans)
