L = list(map(int, input().split()))
s = sum(L)
n = len(L)
if s % n == 0 and s != 0:
    print(s // n)
else:
    print(-1)
