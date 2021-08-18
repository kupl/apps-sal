s = input()
n = len(s)

cnt_r = 0
cnt_b = 0
for c in s:
    if c == "0":
        cnt_r += 1
cnt_b = n - cnt_r
print(2 * min(cnt_r, cnt_b))
