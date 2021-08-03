n = int(input())
a = list(map(int, input().split()))

kind = set(a)
num = len(kind)

diff = n - num
div = (diff - 1) // 2

ans = n - 2 * (div + 1)
print(ans)
