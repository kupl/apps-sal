n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = str(input())

t_list = [c for c in t]
for i in range(k, n):
    if t_list[i] == t_list[i - k]:
        t_list[i] = "x"

score = 0
for hand in t_list:
    if hand == "r":
        score += p
    elif hand == "s":
        score += r
    elif hand == "p":
        score += s

print(score)
