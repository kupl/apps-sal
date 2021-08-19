from collections import defaultdict
(Blue, Red) = (defaultdict(int), defaultdict(int))
N = int(input())
for _ in range(N):
    Blue[input()] += 1
M = int(input())
for _ in range(M):
    Red[input()] += 1
ans = 0
for (word, cnt) in list(Blue.items()):
    temp = cnt - Red[word]
    ans = max(ans, temp)
print(ans)
