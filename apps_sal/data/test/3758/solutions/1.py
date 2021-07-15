import bisect

n = int(input())
s = input()
packmans = []
stars = []
for i in range(n):
    if s[i] == '*':
        stars.append(i)
    elif s[i] == 'P':
        packmans.append(i)

if len(stars) == 0:
    print(0)
    return


def check(t):
    first_to_eat = 0
    for i in range(len(packmans)):
        x = stars[first_to_eat]
        if packmans[i] > x:
            if packmans[i] - x > t:
                return False
            d1 = t - 2 * (packmans[i] - x)
            d2 = (t - (packmans[i] - x)) // 2
            first_to_eat = bisect.bisect_right(stars, packmans[i] + max(d1, d2))
            if first_to_eat < len(stars) and stars[first_to_eat] == packmans[i] + max(d1, d2):
                first_to_eat += 1

        else:
            j = bisect.bisect_right(stars, packmans[i] + t)
            if first_to_eat < len(stars) and stars[first_to_eat] == packmans[i] + t:
                first_to_eat += 1
            first_to_eat = max(j, first_to_eat)
        if first_to_eat >= len(stars):
            return True
    return first_to_eat >= len(stars)


l = 0
r = 2 * n + 1

while r - l > 1:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)

