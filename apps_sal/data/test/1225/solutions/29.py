h = int(input())
ans = 0
n = 1
while h!=0:
    ans += n 
    n *= 2
    h = h//2
print(ans)
