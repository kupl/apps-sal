import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))
ctr = 1
share = 0
for i in range(n):
    if r[i] < b[i]:
        ctr += 1
    elif r[i] > b[i]:
        share += 1
if share == 0:
    print(-1)
else:
    score, rem = divmod(ctr, share)
    if rem == 0:
        print(score)
    else:
        print(score + 1)

# inf.close()
