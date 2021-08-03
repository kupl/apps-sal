N, K = list(map(int, input().split()))

D = list(map(int, input().split()))


def ok(x):
    while x:
        if x % 10 in D:
            return False
        x //= 10
    return True


for i in range(N, 100000):
    if ok(i):
        print(i)
        return
