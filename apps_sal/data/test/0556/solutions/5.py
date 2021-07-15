l, r, k = [int(x) for x in input().split()]
ans = []
a = 1
while a <= r:
    if a >= l:
        ans.append(a)
    a *= k

if ans:
    for num in ans:
        print(num, end = ' ')
else:
    print(-1)

