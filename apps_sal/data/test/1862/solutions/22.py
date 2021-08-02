n = int(input())
x = map(int, input().split(' '))
ans = 0
y = set()
for i in x:
    if i in y:
        y.remove(i)
    else:
        y.add(i)
    ans = max(ans, len(y))
print(ans)
