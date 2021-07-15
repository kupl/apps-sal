n = input()
div = 0
for i in range(len(n)):
    div += int(n[i])
    
if int(n) % div == 0:
    print("Yes")
else:
    print("No")
