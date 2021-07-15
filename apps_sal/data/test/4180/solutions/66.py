num = int(input())
x = ""
cnt = 1000
while x != "pass":
    if cnt >= num:
        x = "pass"
    else:
        cnt += 1000
print(cnt - num)
