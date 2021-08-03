n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = [x - y for x, y in zip(a, b)]

# print(k)
# print(a)
# print(b)
# print(diff)

index = sorted(list(range(len(diff))), key=lambda x: diff[x])
# print(index)

cheat = len([x for x in diff if x < 0])
# print(cheat)
k = max(k, cheat)

bnow = index[:k]
blater = index[k:]

bnow = [a[x] for x in bnow]
blater = [b[x] for x in blater]

# print(bnow)
# print(blater)

print(sum(bnow) + sum(blater))
