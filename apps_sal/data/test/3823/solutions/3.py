n = int(input())
As = list(map(float, input().split()))

B = list(x - int(x) for x in As if x - int(x) > 0.000)
l = len(B)
if l == 0:
    print('{:.3f}'.format(0))
    return

S = sum(x for x in B)

ans = 1e10
for i in range(max(0, l - n), min(l, n) + 1):
    ans = min(ans, abs(i - S))

print('{:.3f}'.format(ans))
