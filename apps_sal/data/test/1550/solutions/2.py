n = int(input())
num = input()

ans = str(num)
for i in range(n):
    d = int(num[i])
    new_num = ''
    for j in range(n):
        dig = (int(num[(i + j) % n]) - d) % 10
        new_num += str(dig)
    ans = min(ans, new_num)

print(ans)

