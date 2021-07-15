q = input()
cnt = [0 for i in range(101)]
can = True
for i in map(int, input().split()):
    cnt[i] += 1
    if i == 50:
        cnt[25] -= 1
        if cnt[25] < 0:
            can = False
    elif i == 100:
        if cnt[50] >= 1 and cnt[25] >= 1:
            cnt[50] -= 1
            cnt[25] -= 1
        elif cnt[25] >= 3:
            cnt[25] -= 3
        else:
            can = False
print('YES' if can else 'NO')

