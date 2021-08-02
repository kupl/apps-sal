def direction(a, b):
    if a[0] == b[0]:
        if a[1] < b[1]:
            return "U"
        return "D"
    if a[0] < b[0]:
        return "R"
    return "L"


def dangerous(a, b):
    if a == "R" and b == "U":
        return True
    if a == "U" and b == "L":
        return True
    if a == "L" and b == "D":
        return True
    if a == "D" and b == "R":
        return True
    return False


n = int(input()) + 1
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

l1 = []
for i in range(n - 1):
    l1.append(direction(l[i], l[i + 1]))
ans = 0
for i in range(n - 2):
    if dangerous(l1[i], l1[i + 1]):
        ans += 1

print(ans)
