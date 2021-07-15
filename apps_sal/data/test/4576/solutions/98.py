A = int(input())  # 500
B = int(input())  # 100
C = int(input())  # 50
X = int(input())  

count = 0
total_price = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            total_price = 500 * i + 100*j + 50*k
            if total_price == X:
                count += 1
print(count)
