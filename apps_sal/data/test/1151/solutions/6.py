n, v = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = [-1]
for i in range(n - 2):
    uk1 = i + 2
    uk2 = n - 1
    while (uk2 - uk1 > 1):
        if l[(uk2 + uk1) // 2] - l[i] <= v:
            uk1 = (uk2 + uk1) // 2
        else:
            uk2 = (uk2 + uk1) // 2
    if l[uk2] - l[i] <= v:
        ans.append((l[uk2] - l[i + 1]) / (l[uk2] - l[i]))
    elif l[uk1] - l[i] <= v:
        ans.append((l[uk1] - l[i + 1]) / (l[uk1] - l[i]))
print(max(ans))
