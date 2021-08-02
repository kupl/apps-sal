ans = int(input())
last = 0
for a in sorted(map(int, input().split())):
    if last > a:
        ans -= 1
    else:
        last = max(a - 1, last + 1)
print(ans)
