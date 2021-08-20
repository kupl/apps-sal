from collections import Counter
N = int(input())
As = list(map(int, input().split()))
cnt = Counter(As)
num = sum([v * (v - 1) // 2 for v in list(cnt.values())])
anss = []
for A in As:
    v = cnt[A]
    ans = num - v * (v - 1) // 2 + (v - 1) * (v - 2) // 2
    anss.append(ans)
print('\n'.join(map(str, anss)))
