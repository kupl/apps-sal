str = input()
heavy = 0
ans = 0
for i in range(0, len(str)):
    if str[i:i + 5] == "heavy":
        heavy += 1
    elif str[i:i + 5] == "metal":
        ans += heavy
print(ans)

