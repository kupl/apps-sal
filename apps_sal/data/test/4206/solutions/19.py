num = input()

curr = 0
ans = 0

for i in range(len(num)):
    curr += int(num[i])
    if curr % 3 == 0:
        ans += 1
        curr = 0
    elif int(num[i]) % 3 == 0:
        ans += 1
        curr = 0
    elif i < (len(num) - 1):
        if (int(num[i]) + int(num[i + 1])) % 3 == 0:
            curr = int(num[i])
print(ans)
