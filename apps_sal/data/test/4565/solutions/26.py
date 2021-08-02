N = int(input())
S = input()
ans = S.count("E")
left = 0
right = ans
for i in S:
    if i == "E":
        right -= 1
        ans = min(ans, right + left)
    if i == "W":
        ans = min(ans, right + left)
        left += 1
print(ans)
