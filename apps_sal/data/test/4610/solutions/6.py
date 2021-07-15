from collections import Counter, deque

_, k = map(int, input().split())
a = [int(i) for i in input().split()]

ans = 0
d = deque(sorted(Counter(a).values()))
while k < len(d):
    ans += d.popleft()
else:
    print(ans)
