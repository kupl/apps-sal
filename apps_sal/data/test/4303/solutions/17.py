n,k = map(int, input().split())
x = list(map(int, input().split()))
minus = [0]
plus = [0]
for i in x:
    if x:
        plus.append(x)
    else:
        minus.append(-x)
k -= 1
ans = 1000000000000000
for i in range(n-k):
    if x[i+k] < 0:
        ans = min(ans, -x[i])
    elif 0 < x[i+k] and x[i] < 0:
        if -x[i] < x[i+k]:
            ans = min(ans, abs(2*(x[i])) + x[i+k])
        else:
            ans = min(ans, 2*x[i+k] + abs(x[i]))
    else:
        ans = min(ans, x[i+k])
    
print(ans)
