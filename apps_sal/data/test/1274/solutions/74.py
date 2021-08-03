import sys
import queue

input_methods = ['clipboard', 'file', 'key']
using_method = 0
input_method = input_methods[using_method]


def IN(): return map(int, input().split())


mod = 1000000007

# +++++


class node:
    def __init__(self, a_val, a_parent=None):
        self.val = a_val
        self.parent = a_parent
        self.right = None
        self.left = None


def main2():
    n, m = IN()
    vl = []
    for n in range(n):
        a, b = IN()
        vl.append((a, b))

    vl.sort(key=lambda x: -x[1])
    ret = 0
    nwdl = [-1] * (m + 1)  # list(range(m+1))
    for a, b in vl:
        j = m - a
        while j >= 0:
            if nwdl[j] == -1:
                nwdl[j] = 0
                ret += b
                break
            j -= 1
        # pa((a,b,m-a,nwdl))
    print(ret)


def main():
    n, m = IN()
    st_day = [[] for _ in range(m + 1)]
    for n in range(n):
        duration, pay = IN()
        if duration > m:
            continue
        st_day[m - duration].append(pay)

    pq = queue.PriorityQueue()
    ret = 0
    for di in range(m + 1):
        day = m - di
        for pay in st_day[day]:
            pq.put(-pay)
        if not pq.empty():
            v = pq.get()
            ret -= v
    print(ret)


# +++++
isTest = False


def pa(v):
    if isTest:
        print(v)


def input_clipboard():
    import clipboard
    input_text = clipboard.get()
    input_l = input_text.splitlines()
    for l in input_l:
        yield l


def __starting_point():
    if sys.platform == 'ios':
        if input_method == input_methods[0]:
            ic = input_clipboard()
            def input(): return ic.__next__()
        elif input_method == input_methods[1]:
            sys.stdin = open('inputFile.txt')
        else:
            pass
        isTest = True
    else:
        pass
        #input = sys.stdin.readline

    ret = main()
    if ret is not None:
        print(ret)


__starting_point()
