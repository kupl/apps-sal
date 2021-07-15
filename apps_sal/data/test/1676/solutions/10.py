
import sys



def main():
    n, b = [int(tok) for tok in sys.stdin.readline().split()]

    td_list = []
    for i in range(n):
        td_list.append([int(tok) for tok in sys.stdin.readline().split()])

    queue = []
    finish = [-1 for i in range(n)]

    for i, (t, d) in enumerate(td_list):


        if len(queue) > 0:
            if queue[0] <= t:
                queue.pop(0)

        if len(queue) == 0 or queue[-1] < t:
            queue.append(t + d)
            finish[i] = t + d
        elif len(queue) == b + 1:
            pass
        else:
            finish[i] = queue[-1] + d
            queue.append(queue[-1] + d)


    print(" ".join([str(f) for f in finish]))


def __starting_point():
    main()

__starting_point()
