N = int(input())
a = 2
ans = ""
for i in range(1000):
    if N % a == 0:
        ans = "0"+ans
    else:
        ans = "1"+ans
        if i % 2 == 0:
            N -= 2**i
        else:
            N += 2**i
    a *= 2
    if N == 0:
        break
print(ans)

