a, b = input().split()
 
a = int(a)
b = int(b.replace('.', ''))
 
ans = a * b // 100
print(ans)
