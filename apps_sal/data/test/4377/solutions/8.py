def mp():
    return map(int, input().split())


a = list(mp())
a.sort(reverse=True)
print(a[0] - a[1], a[0] - a[2], a[0] - a[3])
