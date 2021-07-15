n, m, k = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
inf = [0 for i in range(k + 1)]
stat = [True for i in range(n + 1)]
time = [0 for i in range(n + 1)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(m):
    for j in range(1, n + 1):
        if stat[j]:
            current_core = inf[a[j - 1][i]]
            if current_core == 0 and a[j - 1][i]  != 0:
                inf[a[j - 1][i]] = j
            elif current_core == -1:
                stat[j], time[j] = False, i + 1
            elif a[j - 1][i] != 0:
                stat[current_core], time[current_core] = False, i + 1
                stat[j], time[j] = False, i + 1
                inf[a[j - 1][i]] = -1
    for p in range(len(inf)):
        if inf[p] != -1:
            inf[p] = 0
for i in range(1, n + 1):
    print(time[i])
