N = int(input())
a = list(map(int, input().split()))

seen = [False] * 8
cnt = 0
cnt_3200 = 0
for i in a:
    i = i // 400
    if i >= 8:
        cnt_3200 += 1
    elif (seen[i] == False):
        cnt += 1
        seen[i] = True

if cnt == 0:
    print(1, cnt_3200)
else:
    print(cnt, cnt + cnt_3200)
