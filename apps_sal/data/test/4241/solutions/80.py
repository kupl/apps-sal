s = input()
t = input()

min_cnt = 10000

for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            cnt += 1
    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)
