N = int(input())
S = input()
x = 0
ans = 0

for i in S:
    if i == "I":
        x += 1
    elif i == "D":
        x -= 1
    ans = max(ans, x)

print(ans)
