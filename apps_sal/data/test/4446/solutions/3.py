n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))

how_much_to_spend = [0 for _ in range(n)]
for i in range(n):
    if h[i] % (a + b) == 0:
        how_much_to_spend[i] = (a + b - 1) // a
    else:
        how_much_to_spend[i] = ((h[i] % (a + b)) - 1) // a

how_much_to_spend = sorted(how_much_to_spend)
ans = 0
for item in how_much_to_spend:
    if item <= k:
        ans += 1
        k -= item

print(ans)
