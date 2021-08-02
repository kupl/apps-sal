import sys

# @profile


def insert(heap, val):
    idx = len(heap)
    heap.append(val)

    while idx > 0:
        p = (idx - 1) >> 1

        if heap[p] <= heap[idx]: break

        heap[p], heap[idx] = heap[idx], heap[p]

        idx = p

# @profile


def removeMin(heap):
    last = heap.pop()

    L = len(heap)

    if L == 0: return
    heap[0] = last
    idx = 0
    while True:
        l = (idx << 1) + 1
        if l >= L: return

        r = l + 1
        best = r if r < L and heap[r] < heap[l] else l

        if heap[best] >= heap[idx]:
            return

        heap[best], heap[idx] = heap[idx], heap[best]

        idx = best


answer = []
n = int(input())


def main():
    h = []

    all_input = sys.stdin.readlines()

    for q in all_input:
        raw = q.split()

        if raw[0] == "insert":
            v = int(raw[1])
            insert(h, v)
        elif raw[0] == "getMin":
            v = int(raw[1])

            while h and h[0] < v:
                answer.append("removeMin\n")
                removeMin(h)

            if not h or h[0] > v:
                answer.append("insert " + raw[1] + '\n')
                insert(h, v)
        elif h:
            removeMin(h)
        else:
            answer.append("insert 0\n")

        answer.append(q)


def print_answer():
    print(len(answer))
    print("".join(answer))


main()
print_answer()
