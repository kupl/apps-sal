X,Y = map(int, input().split())

ans = 0
for _ in range(100):
    ans += 1
    X *= 2
    if X > Y:
        break
print(ans)
