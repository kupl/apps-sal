n = int(input())
ans = 1
x = 0
for i in range(1, n+1):
    counter = 0
    r = 0+i
    while r%2 == 0:
        r //= 2
        counter += 1
    if x < counter:
        ans = i
        x = counter
print(ans)
