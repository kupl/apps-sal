a, b, c = list(map(int, input().split()))
s = set(map(int, input().split()))
ans = 1
if ans not in s:
    for i in range(0, c):
        x, y = list(map(int, input().split()))
        if ans == x:
            ans = y
        elif ans == y:
            ans = x
        if ans in s:
            break
print(ans)
