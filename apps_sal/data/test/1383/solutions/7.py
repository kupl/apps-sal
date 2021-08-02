from collections import Counter
n, m = list(map(int, input().split()))
a = Counter(list(map(int, input().split())))
b = Counter(list(map(int, input().split())))
dct = {}
variants = Counter()
for i in a:
    if a[i] not in dct:
        dct[a[i]] = []
    dct[a[i]].append(i)
for i in b:
    count = b[i]
    for j in dct[count]:
        if i - j >= 0:
            variants[i - j] += 1
        else:
            variants[i - j + m] += 1
mx = -float('inf')
ans = 0
for i in variants:
    if variants[i] > mx or (variants[i] == mx and i < ans):
        ans = i
        mx = variants[i]
print(ans)
