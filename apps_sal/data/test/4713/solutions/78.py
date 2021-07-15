n = int(input())
ans = list(input())
count = 0
a = set()
for i in range(n):
    if ans[i] == 'I':
        count += 1
        a.add(count)
    elif ans[i] == 'D':
        count -= 1
        a.add(count)

print(max(max(a), 0))
