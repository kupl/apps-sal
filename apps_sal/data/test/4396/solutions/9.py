N = int(input())
list = []
for i in range(N):
    a, b = input().split()
    list.append((float(a), b))
sum = 0
for i in range(N):
    if list[i][1] == "JPY":
        sum += list[i][0]
    else:
        sum += list[i][0] * 380000
print(sum)
