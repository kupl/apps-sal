import sys
input = sys.stdin.readline
lis = {}
counter = 0
N = int(input().rstrip())
for i in range(N):
    str = "".join(sorted(list(input().rstrip())))
    if str in lis:
        lis[str] += 1
        counter += lis[str]
    else:
        lis[str] = 0
print(counter)
