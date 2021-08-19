n = int(input())
l = list(map(int, input().split()))
cnt = 0
stop = -1
for i in range(n):
    if l[i] == 1:
        break
    else:
        stop = i
while l and l[-1] == 0:
    l.pop(-1)
for i in range(stop + 1, len(l)):
    if i <= len(l) - 2:
        if i < len(l) - 1 and l[i] == 0 and (l[i + 1] == 0) or (i > 0 and l[i] == 0 and (l[i - 1] == 0)):
            pass
        elif l[i] == 1 or l[i + 1] == 1 or l[i + 2] == 1:
            cnt += 1
    elif i <= len(l) - 2:
        if l[i + 1] == 1:
            cnt += 1
    elif l[i] == 1:
        cnt += 1
print(cnt)
