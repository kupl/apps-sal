n = int(input())
k = 0
while 1:
    if 2 ** k > n:
        break
    ans = 2 ** k
    k += 1
print(ans)
