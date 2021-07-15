a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0

for i in range(a+1):
    i *= 500
    for j in range(b+1):
        j *= 100
        for k in range(c+1):
            k *= 50
            sum = i + k + j
            if sum == x:
                ans += 1

print(ans)
            

