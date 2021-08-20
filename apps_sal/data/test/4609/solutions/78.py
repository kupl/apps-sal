n = int(input())
cnt_l = {}
for _ in range(n):
    a = int(input())
    if a in cnt_l:
        cnt_l[a] ^= 1
    else:
        cnt_l[a] = 1
print(sum(cnt_l.values()))
