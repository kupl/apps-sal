n = int(input())
maxx = 1
x = input().split()
A = [x]
ans = 1
for i in range(n - 1):
    y = input().split()
    if(y == A[-1]):
        ans += 1
    else:
        ans = 1
    A.append(y)
    if(ans > maxx):
        maxx = ans

print(maxx)
