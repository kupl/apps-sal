n = int(input())
al = list(list(map(int, input().split())) for _ in range(n))
al_s = sorted(al, key=lambda x: x[1])

time_sum = 0
for i in range(n):
    time, limit = al_s[i][0], al_s[i][1]
    time_sum += time
    if limit < time_sum:
        print('No')
        return
else:
    print('Yes')
