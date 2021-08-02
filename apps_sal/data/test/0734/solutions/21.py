a, b = map(int, input().split())
list1 = [*map(int, input().split())]
list1.sort(reverse=True)
ans = 0
neededHeight = list1[0]
for i, j in enumerate(list1[1:]):
    neededHeight = max(min(j, list1[i] - 1), 1)
    ans += j - neededHeight
    if list1[i] > 1:
        ans += neededHeight
    list1[i + 1] = neededHeight
print(ans)
