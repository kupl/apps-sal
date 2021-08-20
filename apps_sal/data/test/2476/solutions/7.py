from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
C = sorted(list(Counter(A).values()), reverse=True)
L = len(C)
B = []
num = C[0]
for (i, c) in enumerate(C):
    for _ in range(num - c):
        B.append(i)
    num = c
for _ in range(num):
    B.append(L)
ans = [N]
for n in range(2, N + 1):
    if n > L:
        ans.append(0)
        continue
    count = 0
    stack = []
    for b in B:
        tmp = b
        while stack:
            if tmp >= n:
                last = stack.pop()
                tmp = tmp + last - n
                count += 1
            else:
                break
        count += tmp // n
        stack.append(tmp % n)
    ans.append(count)
print(*ans, sep='\n')
