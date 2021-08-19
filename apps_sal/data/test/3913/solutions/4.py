n = int(input())
s = input()
a = []
m = int(input())
for i in range(m):
    line = input()
    st = set()
    flag = False  # 无效
    for i in range(n):
        if s[i] == '*':
            st.add(line[i])
        elif s[i] != line[i]:
            flag = True
    for i in range(n):
        if s[i] in st:
            flag = True
            break
    if flag:
        continue
    if len(st) > 0:
        a.append(st)
x = [0 for i in range(30)]
for e in a:
    for t in e:
        x[ord(t) - ord('a')] += 1
ans = 0
for i in range(30):
    if x[i] == len(a):
        ans += 1
print(ans)
# print(x)
# print(a)
