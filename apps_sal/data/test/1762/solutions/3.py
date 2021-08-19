
import heapq
from time import time
from random import random
from sys import stdin, stdout
lines = stdin.readlines()


"""
n = 500000 
k = 33279
lines = [(   str(n)+' '+str(k)  )]
for i in range(n):
    x = int(random()*100000)
    y = 1000000000 + int(random()*10000)
    lines.append(  str(x)+' '+str(y)  )
"""
t1 = time()

n, k = int(lines[0].split()[0]), int(lines[0].split()[1])
a = [int(x.split()[0]) for x in lines[1:]]
b = [int(x.split()[1]) for x in lines[1:]]

heap = []

#heap = PriorityQueueSet()
free_servers = k
answers = []
#global_minimum = 0
heap = [a[i] + b[i] for i in range(k)]
answers = heap[:]
heapq.heapify(heap)
"""
answers = []
for i in range(k):
    will_load = int(a[i]+b[i])
    heap.push(will_load, str(will_load))
    answers.append(will_load)
"""
for i in range(k, n):

    cur_min = int(heapq.heappop(heap))
    will_load = int(max(cur_min, a[i]) + b[i])  # 11111111
    heapq.heappush(heap, will_load)
    # print(will_load)
    answers.append(will_load)

t2 = time()
# print(t2-t1)

stdout.write('\n'.join([str(x) for x in answers]))
