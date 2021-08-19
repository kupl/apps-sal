n = int(input())
work = set()
day = set()
prei = 0
ans = []
for (i, x) in enumerate(map(int, input().split())):
    if x > 0:
        if x in work:
            print(-1)
            break
        if x in day:
            print(-1)
            break
        day.add(x)
        work.add(x)
    if x < 0:
        if -x not in work:
            print(-1)
            break
        work.remove(-x)
        if len(work) == 0:
            ans.append(i - prei + 1)
            prei = i + 1
            day = set()
else:
    if prei != n:
        print(-1)
    else:
        print(len(ans))
        print(*ans)
