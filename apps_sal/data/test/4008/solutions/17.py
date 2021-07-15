from collections import Counter

N, K = map(int, input().split())
a = list(map(int, input().split()))
counter = Counter(a)

if counter.most_common(1)[0][1] > K or N < K:
    print("NO")
    return

color_table = {}

current_color = 0
for k, v in counter.items():
    color_table[k] = current_color
    current_color = (current_color + v) % K

ans = [0]*N
for i, n in enumerate(a):
    ans[i] = (color_table[n] % K) + 1
    color_table[n] += 1

print("YES")
print(*ans, sep=" ")
