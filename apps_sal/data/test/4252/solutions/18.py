n = int(input())
s = input().strip()
ans = 0
count = 0
flag = 0
for i in range(n):
    if flag == 0:
        if s[i] == "x":
            count += 1
            flag = 1
    else:
        if s[i] == "x":
            count += 1
        else:
            if count >= 3:
                ans += count - 2
            count = 0
            flag = 0
if flag == 1:
    if count >= 3:
        ans += count - 2
print(ans)
