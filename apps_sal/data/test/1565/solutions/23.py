l = int(input())
num = input()

smallest = 1000000
points = []
for i, c in enumerate(num):
    if i == 0:
        continue
    if (c != '0'):
        if max(i, l - i) < smallest:
            smallest = max(i, l - i)
            points.clear()
        if max(i, l - i) == smallest:
            points.append(i)


ans = int("9" * 100000)
for val in points:
    ans = min(ans, int(num[:val]) + int(num[val:]))

print(ans)
