ss = list(input())
tt = list(input())
cnt = 0
for i in range(len(ss)):
    if ss[i] != tt[i]:
        cnt += 1
print(cnt)
