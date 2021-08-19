(a, b, x, y) = list(map(int, input().split()))
ida = a * 2
idb = b * 2 + 1
diff = abs(ida - idb)
ans = 0
if 2 * x <= y:
    ans = diff * x
else:
    ans = x + diff // 2 * y
print(ans)
