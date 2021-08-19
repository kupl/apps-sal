str_line = input().split(' ')
num = int(str_line[0])
kind = int(str_line[1])
ans = kind
for i in range(num - 1):
    ans *= kind - 1
print(ans)
