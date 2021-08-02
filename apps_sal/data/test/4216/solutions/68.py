from math import floor, sqrt
N = int(input())
def f(x, y): return len(str(x)) if x > y else len(str(y))


ans = len(str(N))
for a in range(1, floor(sqrt(N)) + 1):
    if N % a == 0:
        ans = min(ans, f(a, N // a))
print(ans)
