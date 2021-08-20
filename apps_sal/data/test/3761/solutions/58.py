s = input()
(x, y) = list(map(int, input().split()))
C = [len(fs) for fs in s.split('T')]


def f(cs, t):
    dp = {0}
    for c in cs:
        dp = {i + c for i in dp} | {i - c for i in dp}
    return t in dp


ans = 'Yes' if f(C[2::2], x - C[0]) and f(C[1::2], y) else 'No'
print(ans)
