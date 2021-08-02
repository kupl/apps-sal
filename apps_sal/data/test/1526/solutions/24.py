import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

a = sorted(inl())
n = a[2] - a[1] + a[2] - a[0]
print((n + 2 - 1) // 2 + 1 if n % 2 else n // 2)
