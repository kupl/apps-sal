n = int(input())
s = input()
t = input()

cnt_s_a = 0
cnt_t_a = 0
for i in range(n):
    if s[i] == "a":
        cnt_s_a += 1
    if t[i] == "a":
        cnt_t_a += 1
if (cnt_t_a + cnt_s_a) % 2 == 1:
    print(-1)
    return

b_a = []
a_b = []

for i in range(n):
    if s[i] == "a" and t[i] == "b":
        a_b.append(i)
    if s[i] == "b" and t[i] == "a":
        b_a.append(i)

ans = []
for i in range(len(a_b) // 2):
    ans.append((a_b[2 * i] + 1, a_b[2 * i + 1] + 1))
for i in range(len(b_a) // 2):
    ans.append((b_a[2 * i] + 1, b_a[2 * i + 1] + 1))

if len(a_b) % 2 == 1:
    ans.append((a_b[-1] + 1, a_b[-1] + 1))
    ans.append((a_b[-1] + 1, b_a[-1] + 1))
print(len(ans))
for i in ans:
    print(*i)
