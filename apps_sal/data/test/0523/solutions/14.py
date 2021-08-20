(n, m) = map(int, input().split())
ls = set()
final = ''
for i in range(n):
    s = input()
    if s[::-1] in ls:
        ls.remove(s[::-1])
        final = s + final + s[::-1]
    else:
        ls.add(s)
for s in ls:
    flag = True
    for i in range(m // 2):
        if s[i] != s[m - i - 1]:
            flag = False
    if flag:
        final = final[0:len(final) // 2] + s + final[len(final) // 2:]
        break
print(len(final))
print(final)
