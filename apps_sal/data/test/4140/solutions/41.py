s = input()
n = len(s)
l = [0 for _ in range(n)]
for i in range(n):
    if s[i] == '1':
        l[i] = 1

brack = [0 if i % 2 == 1 else 1 for i in range(n)]
white = [1 if i % 2 == 1 else 0 for i in range(n)]

cnt_1, cnt_2 = 0, 0
for i in range(n):
    cnt_1 += l[i] ^ brack[i]
    cnt_2 += l[i] ^ white[i]
print((min(cnt_1, cnt_2)))
