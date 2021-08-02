n = int(input())
s = input()
seed1 = ["S", "W"]
ans = ["SS", "SW", "WS", "WW"]
for i in s[1:]:
    for k, v in enumerate(ans):
        now = 0 if i == "o" else 1
        now = (now + seed1.index(v[-1]) + seed1.index(v[-2])) % 2
        if now:
            ans[k] += "W"
        else:
            ans[k] += "S"
now = 0 if s[0] == "x" else 1
for i in ans:
    now2 = (now + seed1.index(i[-2]) + seed1.index(i[1]) + seed1.index(i[0])) % 2
    if (i[0] == i[-1]) and now2:
        print(i[:-1])
        return
print(-1)
