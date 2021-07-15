a, b = [i for i in input().split()]
t = int(a + b)
ans = 'No'
n = 1
while n*n <= t:
    if n*n == t:
        ans = 'Yes'
    n += 1
print(ans)

