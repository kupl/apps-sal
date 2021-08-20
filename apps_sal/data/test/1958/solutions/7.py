(n, p) = map(int, input().split())
li = []
for _ in range(n):
    s = input()
    li.append(s)
li = li[::-1]
count = 0
total = 0
for i in li:
    if i == 'halfplus':
        count = count * 2 + 1
        total = total + int(count / 2 * p)
    else:
        count = count * 2
        total = total + int(count / 2 * p)
print(total)
