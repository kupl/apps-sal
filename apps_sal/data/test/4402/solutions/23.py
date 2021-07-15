A,B =list(map(int,input().split()))

if A > 12:
    ans = B
elif A < 6:
    ans = 0
else:
    ans = B//2
print(ans)




