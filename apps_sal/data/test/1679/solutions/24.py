n = int(input())
line = input()

ans = 0
for s in line.split("0"):
    ans *= 10
    ans += len(s)

print(ans)
