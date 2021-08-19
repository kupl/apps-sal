(s, t) = (input(), input())
ans = 'z' * len(s)
for i in range(len(s) - len(t) + 1):
    pre = s[:i].replace('?', 'a')
    for (x, y) in zip(list(s[i:]), list(t)):
        if x != '?' and x != y:
            break
        pre += y
    else:
        pre += s[i + len(t):].replace('?', 'a')
        ans = min(ans, pre)
print(ans if ans != 'z' * len(s) else 'UNRESTORABLE')
