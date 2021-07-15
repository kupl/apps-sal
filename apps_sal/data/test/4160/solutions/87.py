x = int(input())
co = 100
i = 0
while co < x:
    co += co // 100
    i += 1
print(i)
