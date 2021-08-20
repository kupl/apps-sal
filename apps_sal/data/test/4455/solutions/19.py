from collections import defaultdict
(n, k) = input().split()
(n, k) = [int(n), int(k)]
prog_power = defaultdict(set)
prog = []
for (ind, x) in enumerate(input().split()):
    prog_power[int(x)].add(ind + 1)
    prog.append(int(x))
m = defaultdict(set)
for i in range(k):
    (a1, a2) = input().split()
    (a1, a2) = [int(a1), int(a2)]
    if prog[a1 - 1] > prog[a2 - 1]:
        m[a1].add(a2)
    elif prog[a1 - 1] < prog[a2 - 1]:
        m[a2].add(a1)
power = {}
sum = n
for i in sorted(prog_power.keys(), reverse=True):
    sum -= len(prog_power[i])
    power[i] = sum
for (ind, i) in enumerate(prog):
    mentor = power[i] - len(m[ind + 1])
    print(mentor, end=' ')
