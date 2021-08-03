n, k = map(int, input().split())
a = list(input().split())

for i in range(n, 100001):
    flg = True
    s = str(i)
    for j in range(len(s)):
        if s[j] in a:
            flg = False
            break
    if flg:
        break
print(i)
