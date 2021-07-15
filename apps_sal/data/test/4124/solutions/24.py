s = list(input())
t = list(input())
ans = len(s) + len(t)
i = len(s) - 1
j = len(t) - 1
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        ans -= 2
        i -= 1
        j -= 1
    else:
        break
print(ans)
