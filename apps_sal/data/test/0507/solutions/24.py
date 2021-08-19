n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
not_equals = []
for i in range(n):
    if a[i] != b[i]:
        not_equals.append(i)
if len(not_equals) == 1:
    x = 1
    while x <= n and x in a and (x in b):
        x += 1
    a[not_equals[0]] = x
    print(*a)
else:
    a2 = [elem for elem in a]
    a2[not_equals[0]] = b[not_equals[0]]
    if sorted(a2) == [i for i in range(1, n + 1)]:
        print(*a2)
    else:
        a2 = [elem for elem in a]
        a2[not_equals[1]] = b[not_equals[1]]
        print(*a2)
