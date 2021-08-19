n = int(input())
s = str(input())
count = 0
used = []
if n > 26:
    print(-1)
else:
    for i in s:
        if i not in used:
            count += s.count(i) - 1
            used.append(i)
    print(count)
