n = input()
renzoku = 0
ans = 0
for i in n:
    if i == "R":
        renzoku += 1
        ans = max(renzoku, ans)
    else:
        renzoku = 0

print(ans)
