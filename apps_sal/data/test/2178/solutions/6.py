
def main():
    n = int(input())
    a = list([int(x) for x in input().split(" ")])
    b = list([int(x) for x in input().split(" ")])
    now = 0
    ans = []
    h = set()
    for i in range(n):
        count = 0
        while b[i] not in h:
            h.add(a[now])
            now += 1
            count += 1
        ans.append(str(count))
    print(" ".join(ans))


def __starting_point():
    main()

__starting_point()
