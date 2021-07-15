N = int(input())
for i in range(N,1000):
    moji = str(i)
    if (moji[0] == moji[1]) and (moji[1] == moji[2]):
        break
        
print(i)
