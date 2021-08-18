from functools import reduce

s = input()
x, y = list(map(int, input().split()))

C = [len(fs) for fs in s.split('T')]


def f(cs, t):
    return t in reduce(
        lambda acc, c: {i + c for i in acc} | {i - c for i in acc},
        cs,
        {0}
    )


ans = (
    'Yes' if f(C[2::2], x - C[0]) and f(C[1::2], y) else
    'No'
)
print(ans)
