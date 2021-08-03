from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
freq = defaultdict(list)

for i in range(n):
    for j in range(i + 1, n + 1):
        freq[sum(nums[i:j])].append((i + 1, j))

ans = []
for k in freq:
    l = freq[k]
    l.sort(key=lambda x: x[1])
    tmp = [l[0]]
    for i, j in l:
        if i <= tmp[-1][1]:
            continue
        tmp.append([i, j])

    if len(tmp) > len(ans):
        ans = tmp
print(len(ans))
for i, j in ans:
    print(i, j)
