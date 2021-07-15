n, k = map(int, input().split())
s = input()
ss = ''
for i in range(n):
    if i == k-1:
        ss += s[i].lower()
    else:
        ss += s[i]
print(ss)
