n = int(input())
judge = ['AC', 'WA', 'TLE', 'RE']
cnt = [0] * 4
for _ in range(n):
    s = input()
    cnt[judge.index(s)] += 1
for i in range(4):
    print(judge[i], 'x', cnt[i])
