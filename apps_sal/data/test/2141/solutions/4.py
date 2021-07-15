n = int(input())

for i in range(n):
    print("".join("WB"[(i+j)%2] for j in range(n)))
