from sys import setrecursionlimit
import threading


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] < a[-1]:
        a = a[::-1]
    mem = [{} for x in range(n)]

    def strokes(ind, height):
        if ind >= n:
            return 0
        if height in mem[ind]:
            return mem[ind][height]
        if height >= a[ind]:
            mem[ind][height] = strokes(ind + 1, a[ind])
            return mem[ind][height]
        else:
            one = strokes(ind + 1, height) + 1
            two = strokes(ind + 1, a[ind]) + a[ind] - height
            mem[ind][height] = min(one, two)
            return mem[ind][height]
    print(strokes(0, 0))


setrecursionlimit(10000)
threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()
