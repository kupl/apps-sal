n = int(input())
arr = []
for i in range(n - (1 - n % 2), 0, - 2):
    arr.append(i)
    
for i in range(n - n % 2, 1, -2):
    if abs(i - arr[-1]) != 1:
        arr.append(i)
        
print(len(arr))
for i in arr:
    print(i, end=" ")
    
