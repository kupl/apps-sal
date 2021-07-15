N = int(input())
a=[int(i) for i in input().split()]

sum_a=sum(a)
ans = 10**11
x=0
for i in range(N-1):
    x += a[i]
    diff = abs(sum_a - 2 * x)
    if diff<ans:
        ans=diff


print(ans)

