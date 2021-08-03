def read():
    inputs = input().strip()
    return list(map(int, inputs.split()))


def read_pair():
    return map(int, input().split(' '))


def read_str():
    return map(str, input().split(' '))


n = int(input())
ans1 = 0
ans2 = 0
for i in range(n):
    x, y = read_pair()
    ans1 += x
    ans2 += y
print(min(ans1, n - ans1) + min(ans2, n - ans2))
