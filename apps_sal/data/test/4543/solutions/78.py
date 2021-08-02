a, b = map(str, input().split())
ab = int(a + b)

ans = "No"
for i in range(1010):
    x = i**2
    if x == ab:
        ans = "Yes"
        break

print(ans)
