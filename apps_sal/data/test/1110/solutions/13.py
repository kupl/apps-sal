n = int(input())
pushes = 0

for i in range(n):
    pushes += ((i + 1) * (n - i)) - i
    
print(pushes)
