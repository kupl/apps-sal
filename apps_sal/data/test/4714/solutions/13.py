A, B = map(int, input().split())
count = 0

for i in range(A, B+1):
    if str(i)[0] == str(i)[4]:
        if str(i)[1] == str(i)[3]:
            count += 1
            
print(count)
