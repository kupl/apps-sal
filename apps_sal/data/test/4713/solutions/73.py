n = int(input())
s = input()

ans = 0
num = 0
for i in s:
    if i == "I":
        num += 1
        ans = max(ans, num)
    elif i == "D":
        num -= 1
        ans = max(ans, num)

print(ans)
