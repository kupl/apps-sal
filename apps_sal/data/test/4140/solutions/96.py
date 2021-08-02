S = input()
left = S[0]
ans = 0
for i in range(1, len(S)):
    if left == "1" and S[i] == "1":
        left = "0"
        ans += 1
        continue
    elif left == "0" and S[i] == "0":
        left = "1"
        ans += 1
        continue
    else:
        left = S[i]

print(ans)
