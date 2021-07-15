n = int(input())
num = input().split()
first = 0
for i in range(n):
    if (num[i].count('1') + num[i].count('0') != len(num[i])) or (num[i].count('1') > 1):
        first = i
ans = num[first]
for i in range(n):
    if i != first:
        ans += num[i].count('0') * '0'

if not num.count('0'):
    print(ans)
else:
    print('0')
