x, y = map(str, input().split())

if int(ord(x)) < int(ord(y)):
    ans = '<'
elif int(ord(x)) > int(ord(y)):
    ans = '>'
else:
    ans = '='
print(ans)
