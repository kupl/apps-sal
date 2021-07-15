N=int(input())
ans = 0
 
for i in range(1, N+1):
    num = N // i
    if num == 1:
        ans += i
    else:
        ans += num * (i + num * i) / 2
 
print(int(ans))
