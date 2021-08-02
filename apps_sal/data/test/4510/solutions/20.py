from queue import Queue


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    checked = {}
    for a in A:
        checked[a] = False

    q = Queue()
    for i, a in enumerate(A):
        if checked[a]:
            continue
        else:
            checked[a] = True
            q.put(a)
            if q.qsize() > K:
                b = q.get()
                checked[b] = False
    L = q.qsize()
    ans = []
    for i in range(L):
        a = q.get()
        ans.append(a)
    print(L)
    print(' '.join([str(a) for a in ans[::-1]]))


def __starting_point():
    main()


__starting_point()
