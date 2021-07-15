number=int(input())
rem=10**9+1
state=True
for i in range(number):
    numList = list(map(int, input().split()))
    mmin=min(numList[0],numList[1])
    mmax=max(numList[0],numList[1])
    if mmax<=rem:
        rem=mmax
    elif mmin<=rem:
        rem=mmin
    else:
        state=False
        break
if state:
    print("YES")
else:
    print("NO")
