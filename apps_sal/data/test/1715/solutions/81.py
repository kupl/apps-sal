import bisect

a, b, q = map(int, input().split())
s = []
for i in range(a):
    s.append(int(input()))
s.sort()
t = []
for i in range(b):
    t.append(int(input()))
t.sort()

for i in range(q):
    x = int(input())
    temp_s = bisect.bisect(s, x)
    temp_t = bisect.bisect(t, x)
    temp = float("inf")
    if temp_s == 0:
        num = (s[0],)
    elif temp_s == a:
        num = (s[a - 1],)
    else:
        num = (s[temp_s - 1], s[temp_s])
    for j in num:
        temp2 = bisect.bisect(t, j)
        if temp2 == 0:
            num2 = (t[0],)
        elif temp2 == b:
            num2 = (t[b - 1],)
        else:
            num2 = (t[temp2 - 1], t[temp2])
        for k in num2:
            temp = min(temp, abs(x - j) + abs(j - k))
    if temp_t == 0:
        num = (t[0],)
    elif temp_t == b:
        num = (t[b - 1],)
    else:
        num = (t[temp_t - 1], t[temp_t])
    for j in num:
        temp2 = bisect.bisect(s, j)
        if temp2 == 0:
            num2 = (s[0],)
        elif temp2 == a:
            num2 = (s[a - 1],)
        else:
            num2 = (s[temp2 - 1], s[temp2])
        for k in num2:
            temp = min(temp, abs(x - j) + abs(j - k))
    print(temp)
