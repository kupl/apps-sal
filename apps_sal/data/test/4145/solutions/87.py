x = int(input())
for i in range(x, 10**6):
    for j in range(2, int(i**(1 / 2)) + 1):
        if i % j == 0:
            break
    else:
        ans = i
        break
print(ans)
