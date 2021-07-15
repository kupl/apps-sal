n = int(input())
list01 = []
for i in range(n):
    list01.append(int(input()))
print(sum(list01) - max(list01) // 2)
