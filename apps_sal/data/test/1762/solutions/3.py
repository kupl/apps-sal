import heapq
from time import time
from random import random
from sys import stdin, stdout
lines = stdin.readlines()
"\nn = 500000 \nk = 33279\nlines = [(   str(n)+' '+str(k)  )]\nfor i in range(n):\n    x = int(random()*100000)\n    y = 1000000000 + int(random()*10000)\n    lines.append(  str(x)+' '+str(y)  )\n"
t1 = time()
(n, k) = (int(lines[0].split()[0]), int(lines[0].split()[1]))
a = [int(x.split()[0]) for x in lines[1:]]
b = [int(x.split()[1]) for x in lines[1:]]
heap = []
free_servers = k
answers = []
heap = [a[i] + b[i] for i in range(k)]
answers = heap[:]
heapq.heapify(heap)
'\nanswers = []\nfor i in range(k):\n    will_load = int(a[i]+b[i])\n    heap.push(will_load, str(will_load))\n    answers.append(will_load)\n'
for i in range(k, n):
    cur_min = int(heapq.heappop(heap))
    will_load = int(max(cur_min, a[i]) + b[i])
    heapq.heappush(heap, will_load)
    answers.append(will_load)
t2 = time()
stdout.write('\n'.join([str(x) for x in answers]))
