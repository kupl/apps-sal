s1 = input()
s2 = input()
ans = ""
for i, j in zip(s1, s2):
    ans += (i + j)

if len(s1) != len(s2):
    ans += s1[-1]
print(ans)
