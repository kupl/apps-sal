n = int(input())
if(n == 2):
    print(1)
    return
n -= 1
res = 0
for i in range(1, n):
    chk = True
    for j in range(2, i + 1):
        if(n % j == 0 and i % j == 0):
            chk = False
    if(chk):
        res += 1
print(res)
