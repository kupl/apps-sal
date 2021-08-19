def main():
    try:
        while True:
            (n, m) = list(map(int, input().split()))
            a = list(map(int, input().split()))
            result = 0
            for i in range(m):
                (left, right) = list(map(int, input().split()))
                s = sum(a[left - 1:right])
                if s > 0:
                    result += s
            print(result)
    except EOFError:
        pass


main()
