a, b = map(int, input().split())

if a <= b:
    ans = a
    for i in range(b-1):
        ans = ans * 10 + a
else:   
    ans = b     
    for i in range(a-1):
        ans = ans * 10 + b

print(ans)
