n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
a.append(10**10)
ans = []
cand = 1
for i in range(len(a)):
    while cand < a[i]:
        m -= cand
        if m < 0:
            print(len(ans))
            if len(ans) > 0:
                print(*ans)
            return
        ans.append(cand)
        cand += 1

    cand = a[i] + 1

