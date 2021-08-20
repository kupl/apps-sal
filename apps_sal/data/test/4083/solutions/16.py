(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
value_lists = [[] for _ in range(2 * 10 ** 5 + 1)]
for val in arr:
    turn = 0
    while val != 1:
        value_lists[val].append(turn)
        val //= 2
        turn += 1
    value_lists[val].append(turn)
mindist = 999999999
for turns_val in value_lists:
    if len(turns_val) < k:
        continue
    turns_val.sort()
    mindist = min(mindist, sum(turns_val[:k]))
print(mindist)
