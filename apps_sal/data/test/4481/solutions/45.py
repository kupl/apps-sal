def main():
    n = int(input())
    d = dict()
    for _ in range(n):
        s = input()
        if s not in list(d.keys()):
            d[s] = 1
        else:
            d[s] += 1
    mostFrequent = max(d.values())
    ans = []
    for key in list(d.keys()):
        if d[key] == mostFrequent:
            ans.append(key)
    ans.sort()
    for i in ans:
        print(i)


def __starting_point():
    main()


__starting_point()
