n, k = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])

numbers = [[0, 0] for i in range(a[-1]+1)]

for i in range(n):
    op = 0
    
    while a[i] > 0:
        if numbers[a[i]][0] < k:
            numbers[a[i]][0] += 1
            numbers[a[i]][1] += op
        
        a[i] //= 2
        op += 1
        
    numbers[0][0] += 1
    numbers[0][1] += op
    
ans = numbers[0][1]

for number in numbers:
    if number[0] >= k and number[1] < ans: ans = number[1]
        
print(ans)
