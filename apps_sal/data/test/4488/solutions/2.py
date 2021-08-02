a = int(input())
b = int(input())

if b < a:
    ans = 'GREATER'
elif a < b:
    ans = 'LESS'
else:
    ans = 'EQUAL'

print(ans)
