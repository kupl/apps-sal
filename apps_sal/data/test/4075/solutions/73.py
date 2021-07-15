N,M = map(int,input().split())
conditions = []
for i in range(M):
    conditions.append(list(map(int,input().split()))[1:])
compair = list(map(int, input().split()))

master_list = []
for i in range(2 ** N):
    target = list(map(int,'{:010b}'.format(i)))[-N:]
    master_list.append(target)
    
result_list = []
for i in master_list:
    prepair_line = []
    for j in conditions:
        total = 0
        for k in j:
            total += i[k-1]
        prepair_line.append(total % 2)
    result_list.append(prepair_line)

cnt = 0
for i in result_list:
    if compair == i:
        cnt += 1

print(cnt)
