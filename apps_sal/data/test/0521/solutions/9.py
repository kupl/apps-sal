arri = lambda: [int(s) for s in input().split()]
arrf = lambda: [float(s) for s in input().split()]

n = int(input())
s = input()
l = '?'
flag = True
for c in s:
    if l == c and c != '?':
        flag = False
    l = c
cnt = 0
for i in range(1, n - 1):
    if s[i] == '?' and s[i - 1] != '?' and s[i+1] != '?' and s[i - 1] != s[i + 1]:
        cnt += 1
if cnt == s.count('?'):
    flag = False
print('Yes' if flag else 'No')

