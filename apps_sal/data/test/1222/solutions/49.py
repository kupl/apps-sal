import heapq
K = int(input())


def NewLun(strX):
    if strX[-1] != '0' and strX[-1] != '9':
        intX0 = int(strX[-1])
        heapq.heappush(Lun, int(strX + str(intX0 + 1)))
        heapq.heappush(Lun, int(strX + str(intX0)))
        heapq.heappush(Lun, int(strX + str(intX0 - 1)))
    elif strX[-1] == '0':
        heapq.heappush(Lun, int(strX + '0'))
        heapq.heappush(Lun, int(strX + '1'))
    else:
        heapq.heappush(Lun, int(strX + '9'))
        heapq.heappush(Lun, int(strX + '8'))


Lun = [i for i in range(1, 10)]
heapq.heapify(Lun)
for _ in range(K):
    Ans = heapq.heappop(Lun)
    NewLun(str(Ans))
print(Ans)
