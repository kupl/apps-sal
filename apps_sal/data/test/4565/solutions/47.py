n = int(input())
s = list(input())
cnt = 0
ans_list = [0]
e_cnt = 0

for i in range(1, n):
    if s[i - 1] == "E" and s[i] == "E":
        cnt -= 1
        e_cnt += 1
    if s[i - 1] == "E" and s[i] == "W":
        cnt -= 0
    if s[i - 1] == "W" and s[i] == "E":
        cnt += 0
        e_cnt += 1
    if s[i - 1] == "W" and s[i] == "W":
        cnt += 1
    ans_list.append(cnt)

print(min(ans_list) + e_cnt)
