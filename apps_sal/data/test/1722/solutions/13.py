from collections import Counter
n = int(input())
counts = Counter()
for _ in range(n):
    name = input()
    counts[name[0]] += 1
ans = 0
for (letter, count) in counts.items():
    a = count // 2
    b = count - a
    ans += a * (a - 1) // 2
    ans += b * (b - 1) // 2
print(ans)
