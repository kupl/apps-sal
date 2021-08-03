s = input()
mae = ""
cnt = 0
for i in range(len(s)):
    if mae == s[i]:
        cnt += 1
        if s[i] == "0":
            mae = "1"
        else:
            mae = "0"

    else:
        mae = s[i]

print(cnt)
