import sys
input = sys.stdin.readline
N = int(input())
S = input()
cnt = 0
tmp = []
for s in S:
    tmp.append(s)
    if len(tmp) <= 2:
        continue
    elif tmp[-1] == 'x' and tmp[-2] == 'o' and (tmp[-3] == 'f'):
        cnt += 1
        for _ in range(3):
            tmp.pop()
print(N - cnt * 3)
