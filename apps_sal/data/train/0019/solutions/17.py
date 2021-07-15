t = int(input())
for _ in range(t):
    n, k, d = list(map(int, input().split()))
    timetable = list(map(int, input().split()))
    i = 0
    j = d
    used = {}
    for x in range(d):
        if timetable[x] in list(used.keys()):
            used[timetable[x]] += 1
        else:
            used[timetable[x]] = 1
    ans = len(used)
    while j < n:
        if timetable[i] in list(used.keys()):
            used[timetable[i]] -= 1
            if used[timetable[i]] == 0:
                used.pop(timetable[i])
        i += 1
        if timetable[j] in list(used.keys()):
            used[timetable[j]] += 1
        else:
            used[timetable[j]] = 1
        j += 1
        ans = min(ans, len(used))
    print(ans)

