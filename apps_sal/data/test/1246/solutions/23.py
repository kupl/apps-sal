from heapq import heappush, heappop
from sys import stdin
heap = []
L = []

n, *l = stdin.read().splitlines()
for string in l:
    array = string.split()
    if array[0] == 'insert':
        heappush(heap, int(array[1]))
    elif array[0] == 'getMin':
        key = int(array[1])
        while heap and heap[0] < key:
            heappop(heap)
            L.append('removeMin')
        if not heap or heap[0] > key:
            heappush(heap, key)
            L.append('insert ' + str(key))
    else:
        if heap:
            heappop(heap)
        else:
            L.append('insert 0')
    L.append(string)

print(len(L))
print('\n'.join(L))
