import sys
input = sys.stdin.readline

t = int(input())

best = [[-1 for x in range(10)] for y in range(151)]

for pp in range(1100):
    total = 0
    for kk in range(10):
        l = list(str(pp + kk))
        l = [int(v) for v in l]
        total += sum(l)
        if total < 151 and best[total][kk] == -1:
            best[total][kk] = pp

my_list = []

num = 900
for abc in range(3, 17):
    for pr in range(9):
        num += (10**abc)
        my_list.append(num)

for rrr in my_list:
    for hh in range(200):
        pp = rrr + hh
        total = 0
        for kk in range(10):
            l = list(str(pp + kk))
            l = [int(v) for v in l]
            total += sum(l)
            if total < 151 and best[total][kk] == -1:
                best[total][kk] = pp

for _ in range(t):
    a, b = list(map(int, input().split()))
    print(best[a][b])
