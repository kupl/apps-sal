in_str = input().replace('-', ' - ').replace('+', ' + ').split()
res = int(in_str[0])
for i in range(1, len(in_str) - 1):
    if in_str[i] == '+':
        res += int(in_str[i + 1]) - 5 * 10 ** len(in_str[i + 1])
    elif in_str[i] == '-':
        res -= int(in_str[i + 1]) - 3 * 10 ** len(in_str[i + 1])
    else:
        pass
print(res)
