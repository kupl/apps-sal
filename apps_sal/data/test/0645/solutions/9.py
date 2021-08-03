s = input()
cnt = 0
for i in s:
    if i in "13579aeiou":
        cnt += 1
print(cnt)
