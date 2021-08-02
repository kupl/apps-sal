n = int(input())
work = []
for i in range(n):
    a, b = list(map(int, input().split()))
    work.append((a, b))
work = sorted(work, key=lambda x: (x[1], x[0]))

t = 0
for time, limit in work:
    t += time
    if t > limit:
        print('No')
        return
print('Yes')
