n = int(input())
s = [0]
mins = 1000
for i in range(n):
    tmp = int(input())
    s.append(tmp)
    if tmp % 10 != 0:
        mins = min(mins, tmp)
if sum(s) % 10 == 0:
    if mins == 1000:
        print((0))
    else:
        print((sum(s) - mins))
else:
    print((sum(s)))
