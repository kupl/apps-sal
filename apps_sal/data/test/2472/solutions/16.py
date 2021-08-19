import itertools
n = int(input())
work_lst = []
for _ in range(n):
    (a, b) = map(int, input().split())
    work_lst.append((a, b))
work_lst.sort(key=lambda x: x[1])
work_acc = [i[0] for i in work_lst]
work_acc = itertools.accumulate(work_acc)
work_dead = [i[1] for i in work_lst]
for (x, dead) in zip(work_acc, work_dead):
    if x > dead:
        print('No')
        break
else:
    print('Yes')
