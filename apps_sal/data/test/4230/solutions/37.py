x, n = list(map(int, input().split()))
p = [int(v) for v in input().split()]
ans = None
if x not in p:
    ans = x
else:
    diff = 101
    for i in range(0, max(p) + 2):

        if abs(x - i) < diff and i not in p:
            ans = i
            diff = abs(x - i)
print(ans)
