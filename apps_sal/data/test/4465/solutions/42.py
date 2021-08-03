import sys
input = sys.stdin.readline
def ins(): return input().rstrip()
def ini(): return int(input().rstrip())
def inm(): return map(int, input().split())
def inl(): return list(map(int, input().split()))


a, b = inm()
print(a * b - 1 * a - 1 * b + 1)
