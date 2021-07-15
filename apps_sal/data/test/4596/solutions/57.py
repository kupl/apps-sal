n = int(input())
data = list(map(int,input().split()))
bool = True
count = 0
while bool:
    for i in range (n):
        if data[i] % 2 != 0:
            bool = False
        data[i] = data[i] // 2
    if bool == False:
        print(count)
    count += 1

