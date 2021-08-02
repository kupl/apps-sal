n, a, b = list(map(int, input().split()))
a -= 1
ans = (a + b) % n + 1
print(ans)
