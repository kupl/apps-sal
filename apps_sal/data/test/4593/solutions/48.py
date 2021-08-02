a = int(input())
ans = 0
i = 1
while i * i <= a:
    for j in range(1, 1000):
        if i**j <= a and ans < i**j:
            ans = i**j
        if i**j > a:
            break
    i += 1
print(ans)
