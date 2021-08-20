n = int(input())
a = input()
b = input()


def cnt(a, b):
    (a, b) = (int(a), int(b))
    (a, b) = (min(a, b), max(a, b))
    return min(b - a, a + 10 - b)


ans = 0
for i in range(n):
    ans += cnt(a[i], b[i])
print(ans)
