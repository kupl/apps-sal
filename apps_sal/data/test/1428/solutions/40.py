from itertools import permutations


def main():
    (n, c) = list(map(int, input().split()))
    d = [[int(x) for x in input().split()] for _ in range(c)]
    g = [[int(x) - 1 for x in input().split()] for _ in range(n)]
    count = [{}, {}, {}]
    for i in range(n):
        for j in range(n):
            now = g[i][j]
            index = (i + j + 2) % 3
            if now in count[index % 3]:
                count[index % 3][now] += 1
            else:
                count[index % 3][now] = 1
    answer = float('inf')
    for color in permutations([i for i in range(c)], 3):
        now_answer = 0
        for i in range(3):
            for (before_color, num) in list(count[i].items()):
                now_answer += d[before_color][color[i]] * num
        answer = min(answer, now_answer)
    print(answer)


def __starting_point():
    main()


__starting_point()
