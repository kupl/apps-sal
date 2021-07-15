k = int(input())
n = 7
n = n%k
j = 0
i = 1
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    return
if n == 0:
    print(i)
    return
while n != 0:
    j = n
    n = (n*10 + 7) % k 
    if j == n:
        print(-1)
        return
    i += 1

print(i)
