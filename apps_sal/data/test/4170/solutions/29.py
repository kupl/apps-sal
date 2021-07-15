N = int(input())
H = list(map(int, input().split()))

result = 0
count = 0
for i in range(len(H)-1):
    if H[i+1] <= H[i]:
        count += 1
        if i == len(H) - 2:
            result = max(result, count)
    else:
        result = max(result, count)
        count = 0
    before_h = H
    
print(result)
