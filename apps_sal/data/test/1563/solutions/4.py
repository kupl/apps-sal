from collections import defaultdict
n, m = list(map(int, input().split()))
colour = [0] + list(map(int, input().split()))
mx, ans = 0, min(colour[1:])
count = defaultdict(set)
for _ in range(m):
    a, b = list(map(int, input().split()))
    if colour[a] != colour[b]:
        count[colour[a]].add(colour[b])
        count[colour[b]].add(colour[a])
for colour in count:
    if len(count[colour]) > mx:
        mx = len(count[colour])
        ans = colour
    elif len(count[colour]) == mx and colour < ans:
        ans = colour
print(ans)
