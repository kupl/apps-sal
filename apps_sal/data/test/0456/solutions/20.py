n = int(input())
s = input()
x = 0
flag = 0
while x < len(s) - 2:
    if s[x: x + 3] == 'ogo':
        right = x
        left = x + 3
        flag = 0
        for i in range(x + 3, len(s) - 1, 2):
            if s[i: i + 2] == 'go' and flag == 0:
                left += 2
            else:
                flag = 1
        s = s[:right] + '***' + s[left:]
    x += 1
print(s)
