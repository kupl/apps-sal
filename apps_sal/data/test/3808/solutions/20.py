n = int(input())
s = input()

count = 0
res = ""
for i in s:
    if i == "(":
        count += 1
    else:
        count -= 1

    if count < -1:
        res = "No"
        break

if res == "":
    if count == 0:
        res = "Yes"
    else:
        res = "No"

print(res)

