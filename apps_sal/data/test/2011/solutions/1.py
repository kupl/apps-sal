import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

val = [0] * n
for i in range(m):
    a, b, cost = info[i]
    a -= 1
    b -= 1
    val[a] -= cost
    val[b] += cost

minus = []
plus = []
for i in range(n):
    if val[i] < 0:
        minus.append([i, -val[i]]) 
    if val[i] > 0:
        plus.append([i, val[i]]) 

ans = []
num1 = 0
for num2, cost in minus:
    a = num2 + 1
    value = cost
    while True:
        if value == 0:
            break
        if num1 >= len(plus):
            break
        if plus[num1][1] <= value:
            ans.append((a, plus[num1][0] + 1, plus[num1][1]))
            value -= plus[num1][1]
            num1 += 1
        else:
            ans.append((a, plus[num1][0] + 1, value))
            plus[num1][1] -= value
            break

print(len(ans))
for i in ans:
    print(*i)
