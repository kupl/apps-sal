str1 = input()
str2 = input()
idx = 0
cnt = 0
for _ in range(len(str1)):
    if str1[idx] != str2[idx]:
        cnt += 1
    idx += 1
print(cnt)
