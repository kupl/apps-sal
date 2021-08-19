from collections import Counter
try:
    while True:
        langs = Counter()
        input()
        for i in input().split():
            langs[int(i)] += 1
        input()
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        result = (0, 0)
        result_index = 1
        for (i, (x, y)) in enumerate(zip(b, c), 1):
            t = (langs[x], langs[y])
            if t > result:
                result = t
                result_index = i
        print(result_index)
except EOFError:
    pass
