ls = [int(i) % 3 for i in input()]
ls.reverse()
cnt = 0
t = 0
s = 0
for (j, i) in enumerate(ls):
    if i == 0 or t + i == 3 or s + i == 3:
        s = 0
        t = 0
        cnt += 1
    else:
        t = (t + i) % 3
        s = i
print(cnt)
