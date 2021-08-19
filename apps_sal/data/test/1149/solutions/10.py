n = int(input())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
k = len(p) + len(q) - 2
for i in range(1, len(p)):
    for j in range(1, len(q)):
        if p[i] == q[j]:
            k -= 1
if k == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
