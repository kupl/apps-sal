n = int(input())
quant = [0] * 5001
numbers = list(map(int, input().split()))
res = []
m = max(numbers)

for i in range(n):
    quant[numbers[i]] += 1

i = 1

while i < m:
    if quant[i] > 0:
        res.append(i)
        quant[i] -= 1
    i += 1
res.append(m)
i = m - 1
while i > 0:
    if quant[i] > 0:
        res.append(i)
        quant[i] -= 1
    i -= 1
    
print(len(res))
print(*res)
