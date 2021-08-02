s = input()
int_s = int(s)

cnt = 0
for i in range(len(s)):
    cnt += int(s[i])

if int_s % cnt == 0:
    print("Yes")
else:
    print("No")
