n = int(input())
name_list = [0, 0, 0, 0, 0]
alp = ["M", "A", "R", "C", "H"]
for i in range(n):
    s = input()
    if s[0] in alp:
        name_list[alp.index(s[0])] += 1
ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += name_list[i] * name_list[j] * name_list[k]

print(ans)
