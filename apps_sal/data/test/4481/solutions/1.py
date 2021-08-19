n = int(input())
s_l = [input() for _ in range(n)]
d = {}
for s in s_l:
    try:
        d[s] += 1
    except:
        d[s] = 1
max_c = max([v for (_, v) in d.items()])
ans = [i for (i, v) in d.items() if v == max_c]
for i in sorted(ans):
    print(i)
