from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

counter = Counter(cards)
ans = len(counter)
rest = 0
for num, cnt in counter.items():
    rest += (cnt - 1)

if rest % 2 == 1:
    ans -= 1

print(ans)
