s = input()
cnt = 0
for i in range(4):
    if s[i] == "+":
        cnt += 1
    else:
        cnt -= 1
print(cnt)
