import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
V = list(map(int, input().split()))

ans = 0
counter = Counter(V)
if len(counter) == 1:
    ans = N // 2
elif N == 2:
    ans = 1
else:
    counter1 = Counter(V[0::2])
    counter2 = Counter(V[1::2])

    counter1 = sorted(counter1.items(), key=lambda x: x[1], reverse=True)
    counter2 = sorted(counter2.items(), key=lambda x: x[1], reverse=True)
    if counter1[0][0] == counter2[0][0]:
        ans = N - counter1[1][1] - counter2[0][1]
        ans = min(ans, N - counter1[0][1] - counter2[1][1])
    else:
        ans = N - counter1[0][1] - counter2[0][1]

print(ans)
