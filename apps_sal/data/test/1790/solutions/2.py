def main():
    n = int(input())
    d = dict()
    for i in range(n):
        arr = list(map(int, input().split()))[1:]
        for j in arr:
            if j not in d:
                d[j] = 0
            d[j] += 1
    for t in d.keys():
        if d[t] == n:
            print(t, end=' ')


main()
