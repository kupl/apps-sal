import time

s = input()
flag = False
ans = ""

start = time.time()
for i in s:
    if i == '8' or i == '0':
        ans = i
        break

if len(s) >= 2 and ans == "":
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if divmod(int(s[i] + s[j]), 8)[1] == 0:
                ans = s[i] + s[j]
                break

        if ans != "":
            break

if len(s) >= 3 and ans == "":
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            for k in range(j + 1, len(s)):
                if divmod(int(s[i] + s[j] + s[k]), 8)[1] == 0:
                    ans = s[i] + s[j] + s[k]
                    break
            if ans != "":
                break
        if ans != "":
            break

if ans == "":
    print("NO")
else:
    print("YES")
    print(ans)
finish = time.time()
