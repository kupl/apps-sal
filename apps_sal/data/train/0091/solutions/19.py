t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    used = set()
    ans = []
    used.add(q[0])
    ans.append(q[0])
    cnt = 1
    flag = False
    for i in range(1, n):
        if q[i] == q[i - 1]:
            while cnt in used:
                cnt += 1
            used.add(cnt)
            if q[i] > cnt:
                ans.append(cnt)
            else:
                flag = True
                break
        else:
            used.add(q[i])
            ans.append(q[i])
    if flag:
        print(-1)
    else:
        print(*ans)
