n = input()
a = list(map(int, input().split()))
ans = list()
for i in range(min(a), max(a) + 1):
    cost = 0
    for num in a:
        cost += (num - i)**2
    ans.append(cost)
print(min(ans))
