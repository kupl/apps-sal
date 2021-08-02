import sys
input = sys.stdin.readline
out = sys.stdout


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    query = n // m
    data = {i: 0 for i in range(n)}
    data_stat = {i: set() for i in range(m)}
    for i in range(n):
        data[i] = a[i]
        data_stat[a[i] % m].add(i)
    free = []
    answer = {i: 0 for i in range(n)}
    result = 0
    for i in range(2 * m):
        cur = i % m
        while len(data_stat[cur]) > query:
            elem = data_stat[cur].pop()
            free.append((elem, i))
        while len(data_stat[cur]) < query and free != []:
            elem, mmod = free.pop()
            data_stat[cur].add(elem)
            a[elem] += i - mmod
            result += i - mmod
    print(result)
    for j in a:
        out.write(str(j) + ' ')


def __starting_point():
    main()


__starting_point()
