from collections import defaultdict

T = int(input())

for t in range(T):
    n, T = [int(_) for _ in input().split()]
    A = [int(_) for _ in input().split()]

    pen_in_c = defaultdict(int)
    pen_in_d = defaultdict(int)

    answer = []
    for el in A:
        if pen_in_d[el] < pen_in_c[el]:
            answer.append(1)
            pen_in_d[T - el] += 1
        else:
            answer.append(0)
            pen_in_c[T - el] += 1

    print(' '.join(map(str, answer)))

