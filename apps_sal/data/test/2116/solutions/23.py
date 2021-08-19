(user, item, total) = list(map(int, input().split()))
items = list(map(int, input().split()))
to = 0
for i in range(user):
    a = list(map(int, input().split()))
    for j in a:
        to += items.index(j) + 1
        items.pop(items.index(j))
        items = [j] + items
print(to)
