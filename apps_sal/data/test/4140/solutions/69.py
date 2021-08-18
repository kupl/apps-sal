s = input()
n = len(s)
li = [0] * n

for i in range(n):
    if s[i] == "1":
        li[i] = 1

b = [0] * n
w = [1] * n

for i in range(n):
    if i % 2 == 1:
        b[i] = 1
        w[i] = 0

cnt_1 = 0
cnt_2 = 0
for i in range(n):
    cnt_1 += li[i] ^ b[i]
    cnt_2 += li[i] ^ w[i]
ans = min(cnt_1, cnt_2)
print(ans)
