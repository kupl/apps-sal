def three_num(n):
    result = 0
    while n % 3 == 0:
        n //= 3
        result += 1
    return result


n = int(input())
x = list(map(int, input().split()))
y = set(x)
first = x[0]
max_num = three_num(x[0])
for i in range(1, n):
    temp = three_num(x[i])
    if temp > max_num:
        max_num = temp
        first = x[i]
    elif temp == max_num and first > x[i]:
        first = x[i]
res = []
res.append(first)
y.remove(first)
for i in range(n - 1):
    if res[i] * 2 in y:
        y.remove(res[i] * 2)
        res.append(res[i] * 2)
    else:
        y.remove(res[i] // 3)
        res.append(res[i] // 3)
print(' '.join(map(str, res)))
