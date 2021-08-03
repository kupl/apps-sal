a, b = map(int, input().split())

ans = "No"
for i in range(1, 4):
    if (a * b * i) % 2 != 0:
        ans = "Yes"
        break

print(ans)
