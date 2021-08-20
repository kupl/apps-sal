n = int(input())
languages = {}
s = input().split()
for i in s:
    if i in languages:
        languages[i] += 1
    else:
        languages[i] = 1
m = int(input())
audio = input().split()
subtitles = input().split()
bestm = 1
besta = 0
bests = 0
for i in range(m):
    ad = audio[i]
    sb = subtitles[i]
    ac = 0
    if ad in languages:
        ac = languages[ad]
    sc = 0
    if sb in languages:
        sc = languages[sb]
    if ac > besta or (ac == besta and sc > bests):
        bestm = i + 1
        besta = ac
        bests = sc
print(bestm)
