n, m = (int(t) for t in input().split())
city = [int(t) for t in input().split()]
tower = [int(t) for t in input().split()]


def check(city, tower, r):
    t = 0
    c = 0
    while c < len(city):
        if abs(city[c] - tower[t]) > r:
            # Current tower is too far
            t += 1
            if t == len(tower):
                # Ran out of towers
                return False
        else:
            c += 1
    return True


hi = 2 * (10 ** 9)
lo = 0
out = hi
while hi >= lo:
    mid = (hi + lo) // 2
    if check(city, tower, mid):
        out = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(out)
