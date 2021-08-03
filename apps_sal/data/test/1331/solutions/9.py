n, m, k = list(map(int, input().split()))
times = list(map(int, input().split()))
times.sort()
ans = 0
start = 0
cnt = 0
j = 0
prohibited = []
for i in range(n):
    prohibited += [1]
for i in range(n):
    if times[i] < start + m:
        cnt += 1
    else:
        while times[i] >= start + m:
            if prohibited[j] == 1:
                start = times[j]
                if j != 0:
                    cnt -= 1
            j += 1
        cnt += 1
    if cnt == k:
        cnt -= 1
        ans += 1
        prohibited[i] = 0
if k == 1:
    print(n)
else:
    print(ans)
