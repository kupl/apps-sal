N = int(input())
S = list(map(int, input().split()))
S.sort(reverse=True)
Closed = [False] * (1<<N)
Closed[0] = True
for j in range(N):
    num = 1<<j
    cnt_all = 0
    cnt = 0
    cnt_ = 0
    s_old = -1
    for i, s in enumerate(S):
        if s_old!=s:
            cnt += cnt_
            cnt_ = 0
        c = Closed[i]
        if c:
            cnt_ += 1
        elif cnt > 0:
            Closed[i] = True
            cnt -= 1
            cnt_all += 1
            if cnt_all == num:
                break
        s_old = s
    else:
        print("No")
        return
print("Yes")

