s = input()

ans = 0

for x in s:
    if x == "+":
        ans += 1
    else:
        ans -= 1

print(ans)
