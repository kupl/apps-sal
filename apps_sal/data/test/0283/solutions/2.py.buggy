def not_pr(x):
    return sum(x % i == 0 for i in range(2, x)) != 0


def read(): return map(int, input().split())


n = int(input())
for m in range(1, 1001):
    if not_pr(n * m + 1):
        print(m)
        return
