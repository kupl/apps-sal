N = int(input())

l = list(map(int, input().split()))

counter = 0
flag = 1

while flag == 1:
    for i in range(len(l)):
        if l[i] % 2 != 0:
            flag = 0
            break
        else:
            l[i] = int(l[i] / 2)
    if flag == 1:
        counter += 1

print(counter)
