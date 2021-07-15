n = int(input())
list_a = sorted([int(i) for i in input().split()], reverse=True)
ans = 0
for i in range(0, len(list_a)):
    if i % 2 == 0: ans += list_a[i]
    else: ans -= list_a[i]
print(ans)
