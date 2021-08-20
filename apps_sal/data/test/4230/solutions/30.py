(x, n) = map(int, input().split())
p = [int(s) for s in input().split()]
min_val = 101
for i in range(102):
    if i not in p:
        if abs(i - x) < min_val:
            min_val = abs(i - x)
            ans = i
print(ans)
