a, b = map(int, input().split())

if (a+b)%2 == 0:
    ans=(a+b)//2
else:
    ans=(a+b)//2 +1
print(ans)
