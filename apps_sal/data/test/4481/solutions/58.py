n = int(input())
s = [input() for _ in range(n)]
count = {}

for word in s:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

max_count = max(list(count.values()))
ans = []
for item in count.items():
    (key, value) = item
    if value == max_count:
        ans.append(key)

ans = sorted(ans)
for w in ans:
    print(w)
