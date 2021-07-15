a, b, c = map(str, input().split())
num = int(a + b + c)
 
if num % 4 == 0:
    print("YES")
else:
    print("NO")
