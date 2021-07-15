3

n = int(input())
lst = list(map(int, input().split()))
good = len([i for i in range(n) if lst[i] == i])
best = len([i for i in range(n) if i != lst[i] and lst[lst[i]] == i])
var = len([i for i in range(n) if i != lst[i] and lst[lst[i]] != lst[i]])
print(good + (2 if best else (var > 0)))

