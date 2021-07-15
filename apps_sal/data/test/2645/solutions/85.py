s = input()
ls = len(s)
cnt = [0, 0]
for c in list(s):
    cnt[c != "g"] += 1

if ls % 2 == 1:
    ls -= 1

print((ls//2-cnt[1]))

