from heapq import heappop, heappush
from sys import stdin
(n, *l) = stdin.read().splitlines()
(heap, res) = ([], [])
for s in l:
    array = s.split()
    if array[0] == 'insert':
        heappush(heap, int(array[1]))
    elif array[0] == 'getMin':
        key = int(array[1])
        while heap and heap[0] < key:
            heappop(heap)
            res.append('removeMin')
        if not heap or heap[0] != key:
            heappush(heap, key)
            res.append('insert ' + array[1])
    elif heap:
        heappop(heap)
    else:
        res.append('insert 0')
    res.append(s)
print(len(res))
print('\n'.join(res))
