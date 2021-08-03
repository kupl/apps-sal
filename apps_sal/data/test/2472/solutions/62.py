N = int(input())

AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

sorted_AB = sorted(AB, key=lambda x: (x[1], -x[0]))
worked = 0
for ab in sorted_AB:
    worked += ab[0]
    if worked > ab[1]:
        print('No')
        return

print('Yes')
