from collections import defaultdict
H, W, N = map(int, input().split())

allcase = (H - 2) * (W - 2)

abset = set()
for _ in range(N):
    a, b = map(int, input().split())
    abset.add((a - 1, b - 1))
# print(abset)

memo = defaultdict(int)
for a, b in abset:
    for j in range(-2, 1):
        if a + j < 0 or H - 2 <= a + j:
            continue
        for k in range(-2, 1):
            if b + k < 0 or W - 2 <= b + k:
                continue
            memo[(a + j, b + k)] += 1
# print(memo)

case_list = [0] * 10
for v in memo.values():
    case_list[v] += 1
case_list[0] = allcase - sum(case_list[1:])
# print(case_list)

for i in range(10):
    print(case_list[i])
