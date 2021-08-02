def main():
    N, X, Y = [int(n) for n in input().split(" ")]
    vertex = [[1]] + [[i - 1, i + 1] for i in range(1, N - 1)] + [[N - 2]]
    vertex[X - 1].append(Y - 1)
    vertex[Y - 1].append(X - 1)

    count = [0] * N
    for i in range(N):
        to_visit = [i]
        checked = [0] * N
        steps = [0] * N
        checked[i] = 1

        while len(to_visit) > 0:
            visiting = to_visit.pop(0)
            vs = vertex[visiting]
            step = steps[visiting]
            for v in vs:
                if checked[v] == 0:
                    checked[v] = 1
                    to_visit.append(v)
                    steps[v] = step + 1
                    count[step + 1] += 1

    for c in count[1:]:
        print(int(c / 2))


main()
