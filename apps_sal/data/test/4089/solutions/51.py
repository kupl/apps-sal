x, ar = int(input()) - 1, []
if(x == 0):
    ar.append('a')
else:
    while(x > 0):
        ar.append(chr(97 + x % 26))
        x //= 26
        x = x - 1
        if(x == 0):
            ar.append('a')
ar.reverse()
ans = ''.join(ar)
print(ans)
