num = [int(n) for n in input().split()]
server = [0 for n in range(0,num[0])]
result = list()
num_task = num[1]
temp_ti = 0
for i in range(0,num_task):
    temp_task = [int(n) for n in input().split()]
    time_passed = temp_task[0]-temp_ti
    temp_ti = temp_task[0]
    ###length
    for n in range(0,num[0]):
        server[n] -= time_passed
        server[n] = 0 if(server[n]<0) else server[n]
    if(server.count(0) < temp_task[1]):
        result.append(-1)
    else:
        accumulate_result = 0
        for i in range(0,num[0]):
            if(not bool(server[i])):
                server[i] += temp_task[2]
                temp_task[1] -=1
                accumulate_result +=(i+1)
            if(temp_task[1] ==0):
                break
        result.append(accumulate_result)
for i in range(0,num_task):
    print(result[i])

