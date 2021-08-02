import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
As = [int(x) for x in input().rstrip('\n').split()]
total = sum(As)
half = []
for i in range(N):
    if i == 0:
        half.append((total - sum(As[1::2]) * 2) // 2)
    else:
        half.append(As[i - 1] - half[-1])
print(*[x * 2 for x in half])
