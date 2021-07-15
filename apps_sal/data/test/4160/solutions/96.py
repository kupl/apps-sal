X = int(input())

ans = 0
deposit = 100

while deposit < X:
    deposit = deposit + (deposit // 100)
    ans += 1

print(ans)
