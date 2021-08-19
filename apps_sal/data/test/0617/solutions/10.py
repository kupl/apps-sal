s = input()
mult_list = []
for i in range(len(s)):
    if s[i] == '*':
        mult_list.append(i)
best = eval(s)
for k in mult_list:
    t = '(' + s[:k] + ')' + s[k:]
    q = eval(t)
    if q > best:
        best = q
    t = s[:k + 1] + '(' + s[k + 1:] + ')'
    q = eval(t)
    if q > best:
        best = q
    for j in mult_list:
        if j >= k:
            continue
        if j < k:
            t = s[:j + 1] + '(' + s[j + 1:k] + ')' + s[k:]
            q = eval(t)
            if q > best:
                best = q
print(best)
