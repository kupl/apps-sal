n = int(input())
a = sorted(list(map(int, input().split())))
s = []
for q in a:
    for q1 in s:
        if q % q1 == 0:
            break
    else:
        s.append(q)
print(len(s))

