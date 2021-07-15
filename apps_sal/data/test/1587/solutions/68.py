# RRR..WWW..を目指す
n = int(input())
s = list(input())
w_count, r_count = s.count("W"), s.count("R")
t = list("R" * r_count + "W" * w_count)

ans = 0
for i in range(n):
    if s[i] != t[i]:
        ans += 1
print(min(w_count, r_count, ans // 2))
