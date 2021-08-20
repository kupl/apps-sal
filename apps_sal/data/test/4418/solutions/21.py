from collections import defaultdict
MEMBERS = (4, 8, 15, 16, 23, 42)
progress = {4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
n = int(input())
a = list(map(int, input().split()))
idx = []
counts = defaultdict(int)
for num in a:
    if progress[num] == 0:
        counts[0] += 1
    elif counts[progress[num] - 1] > 0:
        counts[progress[num] - 1] -= 1
        counts[progress[num]] += 1
print(n - counts[5] * 6)
