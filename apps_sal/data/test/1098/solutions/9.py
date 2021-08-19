n = int(input())
t = []
for i in range(n):
    t.append(tuple(map(int, input().split(':'))))

ans = 0

t.sort()
t = t + [(v[0] + 24, v[1]) for v in t]

for i in range(len(t) - 1):
    #print(t[i+1][0] - t[i][0])*60+(t[i+1][1] - t[i][1])
    ans = max(ans, (t[i + 1][0] - t[i][0]) * 60 + (t[i + 1][1] - t[i][1]) - 1)


print('{}:{}'.format(str(ans // 60).rjust(2, '0'), str(ans % 60).rjust(2, '0')))
