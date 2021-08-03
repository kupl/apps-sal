count = int(input())
tree = {'polycarp': 1}
max = 1
for i in range(0, count):
    try:
        rel = input().lower().split(' ')
        if not rel[1] == 'reposted':
            continue
        tree[rel[0]] = tree[rel[2]] + 1
        if tree[rel[0]] > max:
            max = tree[rel[0]]
    except BaseException:
        continue
print(max)
