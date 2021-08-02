s = input()
t = input()

i = len(s) - 1
j = len(t) - 1
ans = 0
while (i >= 0 and j >= 0 and s[i] == t[j]):
    ans += 1
    i -= 1
    j -= 1
print(len(s) + len(t) - 2 * ans)
