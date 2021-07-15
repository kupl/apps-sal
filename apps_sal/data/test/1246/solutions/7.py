import sys
from heapq import *

answer = []
n = int(input())

def main():
    h = []

    all_input = sys.stdin.readlines()

    for q in all_input:
        raw = q.split()

        if raw[0] == "insert":
            v = int(raw[1])
            heappush(h, v)
        elif raw[0] == "getMin":
            v = int(raw[1])

            while h and h[0] < v:
                answer.append("removeMin\n")
                heappop(h)

            if not h or h[0] > v:
                answer.append("insert " + raw[1] + '\n')
                heappush(h, v)
        elif h:
            heappop(h)
        else:
            answer.append("insert 0\n")

        answer.append(q)

def print_answer():
    print(len(answer))
    print("".join(answer))

main()
print_answer()
