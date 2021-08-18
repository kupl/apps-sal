n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = [x - y for x, y in zip(a, b)]


index = sorted(list(range(len(diff))), key=lambda x: diff[x])

cheat = len([x for x in diff if x < 0])
k = max(k, cheat)

bnow = index[:k]
blater = index[k:]

bnow = [a[x] for x in bnow]
blater = [b[x] for x in blater]


print(sum(bnow) + sum(blater))
