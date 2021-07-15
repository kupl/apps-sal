k = int(input())
a = k//50
b = 50-k%50
ans = [a+b-1]*b+[a+50]*(50-b)
print(50)
print(*ans)
