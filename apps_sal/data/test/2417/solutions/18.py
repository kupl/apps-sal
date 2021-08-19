import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_dict = {}
for i in range(n):
    a_dict[a[i]] = i + 1
for i in range(n):
    b[i] = a_dict[b[i]]
b.reverse()
ans = 0
mini = n
for i in range(n):
    if mini >= b[i]:
        mini = b[i]
    else:
        ans += 1
print(ans)
