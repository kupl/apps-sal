int1, int2, rank = map(int, input().split())
kouyaku_list = []
for i in range(1, 100 + 1):
    if int1 % i == 0 and int2 % i == 0:
        kouyaku_list.append(i)

print(kouyaku_list[-rank])
