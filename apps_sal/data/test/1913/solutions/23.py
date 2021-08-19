n = int(input())
zeros = 0
ans = '1'
inp = input().strip().split(' ')
for i in range(n):
    if inp[i] == '0':
        ans = '0'
        zeros = 0
        break
    if inp[i].count('1') > 1 or inp[i].count('1') + inp[i].count('0') != len(inp[i]):
        ans = inp[i]
    else:
        zeros = zeros + inp[i].count('0')
print(ans, '0' * zeros, sep='')
