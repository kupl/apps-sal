n, v = list(map(int, input().split()))
trees = {}
days = set()
for i in range(n):
    a, b = list(map(int, input().split()))
    if a not in trees:
        trees[a] = b
    else:
        trees[a] += b
    days.add(a)

max_days = max(days)
total = 0
for a in range(1, max_days + 1):
    #    print(a)
    #    print(trees)
    prev_collected = 0
    if a - 1 in trees:
        prev_collected = min(trees[a - 1], v)
        trees[a - 1] -= prev_collected
        total += prev_collected
#        print('prev_collected', prev_collected)
    if a in trees:
        collected = min(trees[a], v - prev_collected)
        trees[a] -= collected
        total += collected
#        print('collected', collected)
    elif a - 1 in trees and prev_collected == 0:
        add_collected = min(trees[a - 1], v)
        trees[a - 1] -= add_collected
        total += add_collected
#        print('add_collected', add_collected)

if max_days in trees:
    total += min(trees[max_days], v)
print(total)
