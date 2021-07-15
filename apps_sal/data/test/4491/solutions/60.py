n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
ans = sum(a1)+a2[-1]
memo = ans
a1.reverse()
a2.reverse()
for i in range(n-1):
    memo -=a1[i]-a2[i+1]
    if memo > ans:
        ans = memo
print(ans)

