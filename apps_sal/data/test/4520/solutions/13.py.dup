n, k = list(map(int, input().split()))
ar = []
for i in range(n):
    lolk = list(map(int, input().split()))
    ar.append([lolk[0], 0, lolk[1], i + 1])
    ar.append([lolk[1], 1, lolk[0], i + 1])
ar.sort()
queue = []
kek = 0
ans = 0
ans1 = []
ksjdfks = set()
for time, type, end, lol in ar:
    if lol not in ksjdfks:
        if type == 0:
            kek += 1
            queue.append([time, type, end, lol])
            queue.sort(key=lambda x: x[2])
            if kek > k:
                ans += 1
                ans1.append(queue[-1][3])
                ksjdfks.add(queue[-1][3])
                queue.pop()
                kek -= 1
        else:
            kek -= 1
            queue.pop(queue.index([end, 0, time, lol]))
print(ans)
print(*ans1)
