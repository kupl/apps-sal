from sys import stdin, stdout
from queue import PriorityQueue


def main():
    (n, b) = [int(i) for i in stdin.readline().split()]
    a = [int(i) for i in stdin.readline().split()]
    q = PriorityQueue()
    evens = 0
    for i in range(n - 1):
        if a[i] % 2 == 0:
            evens += 1
        else:
            evens -= 1
        if evens == 0:
            q.put(abs(a[i] - a[i + 1]))
    count = 0
    while not q.empty():
        smallest = q.get()
        if b >= smallest:
            b -= smallest
            count += 1
        else:
            break
    print(count)


main()
