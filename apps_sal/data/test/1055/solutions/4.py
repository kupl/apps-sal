def mp():
    return map(int, input().split())


def f(a):
    if sorted(a) == a:
        return len(a)
    return max(f(a[:len(a) // 2]), f(a[len(a) // 2:]))


n = int(input())
a = list(mp())
print(f(a))
