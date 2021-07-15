import math
X = int(input())
ans = 1
Y = math.floor(math.sqrt(X))
for i in range(2, Y+1):
    for j in range(2, 10):
        a = i**j
        if a <= X:
            ans = max(ans, a)
print(ans)

