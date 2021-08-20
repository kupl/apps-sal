import math
import sys


def cantina():
    datain = []
    queue = []
    for i in range(2):
        datain.append(input().split())
    time = int(datain[0][1])
    for i in range(len(datain[1][0])):
        queue.append(datain[1][0][i])
    for i in range(time):
        queueswap(queue)
    return queue


def queueswap(queue):
    swaps = []
    for i in range(len(queue) - 1):
        if queue[i] == 'B' and queue[i + 1] == 'G':
            swaps.append(i)
    for i in swaps:
        queue[i] = 'G'
        queue[i + 1] = 'B'
    return queue


print(''.join(cantina()))
