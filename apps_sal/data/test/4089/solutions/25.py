a_list = [chr(ord('a') + i) for i in range(26)]
n = int(input())

l_list = []
ans = ''
while n > 0:
    if n % 26 == 0:
        l_list.append(26)
        n = n // 26 - 1
    else:
        l_list.append(n % 26)
        n = n // 26
l_list = l_list[::-1]
for i in l_list:
    ans += a_list[i - 1]
print(ans)
