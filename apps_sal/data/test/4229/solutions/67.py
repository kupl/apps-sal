number = int(input())

ans = 0
i: int
for i in range(1, number + 1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    ans += i

print(ans)
