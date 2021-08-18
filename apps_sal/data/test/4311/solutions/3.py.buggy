s = int(input())
ans = [0] * 1000001
cnt = 1

while True:
    if ans[s] == 0:
        ans[s] += 1

        if s % 2 == 0:
            s = s // 2
        else:
            s = 3 * s + 1
        cnt += 1

    if ans[s] != 0:
        print(cnt)
        return
