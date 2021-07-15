import heapq

n = int(input())
m = n
operations = []
heap = []
for i in range(n):
    s = input() 
    a = s.split()
    if a[0] == 'insert':
        heapq.heappush(heap, int(a[1])) 
    elif a[0] == 'removeMin':
        if heap:
            heapq.heappop(heap)
        else:
            m += 1
            operations.append('insert 1')
    elif a[0] == 'getMin':
        b = int(a[1])
        while heap:
            if heap[0] < b:
                operations.append('removeMin')
                m += 1
                heapq.heappop(heap)
            else:
                break
        else:
            operations.append('insert {}'.format(b))
            m += 1
            heapq.heappush(heap, b)
        if heap[0] > b:
            operations.append('insert {}'.format(b))
            m += 1
            heapq.heappush(heap, b)
    operations.append(s)

print(m)
print('\n'.join(operations))
