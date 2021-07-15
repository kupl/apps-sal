def main():
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[i], "a") for i in range(len(a))]
    c.extend([(b[i], "b") for i in range(len(b))])
    c.sort(key=lambda x: x[0])
    more_then = {}
    count = 0
    for i in range(len(c)):
        if c[i][1] == 'b':
            more_then[c[i][0]] = i - count
            count += 1
    ans = []
    for i in range(len(b)):
        ans.append(more_then[b[i]])
    print(" ".join(map(str, ans)))

def __starting_point():
    main()
__starting_point()
