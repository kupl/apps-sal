(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
i = a[0]
home = a[-1]


def closest_point(i):
    while i not in a:
        i -= 1
    else:
        return i


def count_bikes(i, k, a):
    ans = 0
    while i != home:
        closest_poin = closest_point(i + k)
        if closest_poin == i:
            return -1
            break
        else:
            i = closest_poin
        ans += 1
    return ans


print(count_bikes(i, k, a))
