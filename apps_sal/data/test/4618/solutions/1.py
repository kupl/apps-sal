s = input()
K = int(input())

if K == 1:
    print(sorted(s)[0])
    return

topK = sorted(s)[:min(K, len(s))]

indices = []
for i in range(len(s)):
    if s[i] in topK:
        indices.append(i)

selected = []
for j in range(len(indices)):
    i = indices[j]
    tmp = []
    for k in range(min(K, len(s) - i)):
        tmp.append(s[i:i + k + 1])
    selected.extend(tmp)

selected = sorted(set(selected))

print(selected[K - 1])
