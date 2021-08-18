n = int(input())
A = input().split()
A = [int(k) for k in A]

imposs = False
days = []
curr_empl = set()
day_empl = set()
d_s = 0
for i in range(n):
    e = A[i]
    if e < 0:
        if -e not in curr_empl:
            imposs = True
            break
        curr_empl.remove(-e)
    else:
        if e in day_empl:
            imposs = True
            break
        day_empl.add(e)
        curr_empl.add(e)
    if len(curr_empl) == 0:
        curr_empl = set()
        day_empl = set()
        days.append(i - d_s + 1)
        d_s = i + 1

if imposs or len(curr_empl) > 0:
    print(-1)
else:
    print(len(days))
    print(' '.join([str(di) for di in days]))
