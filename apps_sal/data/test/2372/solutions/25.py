from collections import deque


def main():
    h, w = list(map(int, input().split()))
    cy, cx = list(map(int, input().split()))
    dy, dx = list(map(int, input().split()))

    M = ["##" + input() + "##" for x in range(h)]
    for i in range(2):
        M.insert(0, "#" * (w + 4))
        M.append("#" * (w + 4))

    C = [[-1 if M[j][i] == "." else -2 for i in range(w + 4)] for j in range(h + 4)]
    C[-~cy][-~cx] = 0
    QA, QB = deque(), deque()
    QA.append((-~cy, -~cx, 0))
    W = [[i, j] for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) > 1]

    while QA:
        h, w, c = QA.popleft()
        QB.append((h, w, c))

        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            dh, dw = h + i, w + j
            if C[dh][dw] == -1:
                C[dh][dw] = c
                QA.appendleft((dh, dw, c))

        if QA:
            continue

        while QB:
            h, w, c = QB.popleft()
            for i, j in W:
                dh, dw = h + i, w + j
                if C[dh][dw] == -1:
                    C[dh][dw] = -~c
                    QA.append((dh, dw, -~c))

        if C[-~dy][-~dx] != -1:
            print((C[-~dy][-~dx]))
            return

    print((C[-~dy][-~dx]))


def __starting_point():
    main()


__starting_point()
