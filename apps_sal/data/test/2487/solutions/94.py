def main():
    N = int(input())
    r = 0
    for i in range(1, N + 1):
        r += i * (N + 1 - i)
    for i in range(N - 1):
        u, v = list(map(int, input().split()))
        u, v = min(u, v), max(u, v)
        r -= u * (N + 1 - v)
    return r


print((main()))
