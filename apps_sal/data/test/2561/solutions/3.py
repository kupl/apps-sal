
n = int(input())
for i in range(n):
    b = bin(int(input()))
    count = 0
    for c in b:
        if c == '1':
            count += 1
    print(pow(2, count))
