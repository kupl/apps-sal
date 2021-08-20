(n, k) = map(int, input().split())
l1 = [0] * k
for i in range(n):
    x = int(input())
    l1[x - 1] += 1
ans = 0
odds = 0
for item in l1:
    if item % 2 == 0:
        ans += item
    else:
        ans += item - 1
        odds += 1
if n % 2 == 0:
    print(ans + odds // 2)
else:
    print(ans + (odds - 1) // 2 + 1)
