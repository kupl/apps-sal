(n, m, x) = map(int, input().split())
a = list(map(int, input().split()))
small_cost = 0
big_cost = 0
for i in a:
    if x > i:
        small_cost += 1
    elif x < i:
        big_cost += 1
if small_cost <= big_cost:
    print(small_cost)
else:
    print(big_cost)
