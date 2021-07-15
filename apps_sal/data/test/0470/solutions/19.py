a = list(map(int, input().split()))
s = {}
summa = 0
for i in a:
    summa += i
    try:
        s[i] += 1
    except KeyError:
        s[i] = 1
ans = summa
for i in s:
    if s[i] == 1:
        pass
    else:
        if s[i] == 2:
            ans = min(ans, summa - i * 2)
        else:
            ans = min(ans, summa - i * 3)
print(ans)
