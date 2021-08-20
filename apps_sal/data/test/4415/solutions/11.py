import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
up = [a[0]]
a[0] = -1
for i in range(len(a)):
    if a[i] != -1 and a[i] > up[-1]:
        up.append(a[i])
        a[i] = -1
down = sorted([x for x in a if x != -1], reverse=True)
valid = True
for i in range(1, len(down)):
    if down[i] == down[i - 1]:
        valid = False
        break
if valid:
    print('YES')
    print(len(up))
    print(' '.join([str(x) for x in up]))
    print(len(down))
    print(' '.join([str(x) for x in down]))
else:
    print('NO')
