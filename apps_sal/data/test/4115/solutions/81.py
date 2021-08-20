s = input()
r_s = s[::-1]
cnt = 0
for (a, b) in zip(s, r_s):
    if a != b:
        cnt += 1
print(cnt // 2)
