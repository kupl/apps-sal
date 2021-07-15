n = int(input())

for i in range(110):
    if n % 111 == 0:
        break
    else:
        n += 1
        
print(n)
