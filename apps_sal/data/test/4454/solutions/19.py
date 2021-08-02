def mp():
    return map(int, input().split())


q = int(input())
for qq in range(q):
    n = int(input())
    a = list(mp())
    s = sum(a)
    print((s + n - 1) // n)
