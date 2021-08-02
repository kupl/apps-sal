N = int(input())
K = int(input())
x = list(map(int, input().split()))
print((sum(2 * min(y, K - y) for y in x)))
