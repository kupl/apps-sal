n = int(input())
a = list(map(int, input().split()))
li = [a[0]]
for i in range(n - 1):
    if li[i] < a[i + 1]:
        li.append(a[i + 1])
    else:
        li.append(li[i])
ans = 0
for j in range(n):
    ans += li[j] - a[j]
print(ans)
