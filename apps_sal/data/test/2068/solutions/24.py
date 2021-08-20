n = int(input())
repost_level = {'polycarp': 1}
for i in range(n):
    (name1, _, name2) = input().split()
    repost_level[name1.lower()] = repost_level[name2.lower()] + 1
print(max(repost_level.values()))
