a = str(input())
b = list(a)
if b[len(b) - 1] == 's':
    b.append('es')
else:
    b.append('s')
ans = ''.join(b)
print(ans)
