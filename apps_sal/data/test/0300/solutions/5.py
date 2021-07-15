def main():
    n = int(input())
    def ceil(x):
        if x % 1 == 0:
            return int(x)
        return int(x + 1)
    a = ceil(n * 4.5)
    scores = sorted(list(map(int, input().split())))
    s = sum(scores)
    c = 0
    while s < a:
        s += 5 - scores[c]
        c += 1
    print(c)
    return 0
main()

