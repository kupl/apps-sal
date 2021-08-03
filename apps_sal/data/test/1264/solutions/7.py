n = int(input())
input_str = input()
m = tmp = i = 0
while i < 2 * n - 1:
    if input_str[i] == '0':
        tmp += 1
    elif tmp > 0:
        tmp -= 1
    m = max(m, tmp)
    i += 2
if m == 0:
    print(n - 1)
else:
    print(input_str.count('1') + m)
