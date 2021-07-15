a, b, c = list(map(int, input().split()))
can_listen = b // a
if can_listen >= c:
    ans = c
else:
    ans = can_listen

print(ans)

