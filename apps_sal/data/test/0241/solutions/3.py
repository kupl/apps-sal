n, m, mi, ma = map(int, input().split())
t = list(map(int, input().split()))
mit = min(t)
mat = max(t)
if (mi <= mit and ma >= mat) and (n - m  >= 2 or (n - m >= 1 and (mit == mi or mat == ma)) or (mit == mi and mat == ma)):
    print('Correct')
else:
    print('Incorrect')
