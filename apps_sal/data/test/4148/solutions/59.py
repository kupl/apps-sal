n = int(input())
s = input()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
ans = ''
for i in s:
    ans += abc[abc.index(i) + n]
print(ans)
