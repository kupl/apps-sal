def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    data =[Input() for _ in range(n)]
    ans = 0
    for start, end in data:
        for _ in range(start, end+1):
            ans += 1
    print(ans)


main()
