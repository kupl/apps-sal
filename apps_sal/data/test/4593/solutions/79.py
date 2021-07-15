import sys
 
X = int(sys.stdin.readline())
ans = 0
for i in range(X+1):
    for j in range(2, 11):
        tmp = pow(i, j)
        if tmp <= X:
            ans = max(ans, tmp)
print(ans)
