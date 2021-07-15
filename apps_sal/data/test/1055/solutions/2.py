ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

def rec(a):
    if all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        return len(a)
    x = len(a) // 2
    return max(rec(a[:x]), rec(a[x:]))

ii()
print(rec(li()))
