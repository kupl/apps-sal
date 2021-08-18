
def main():
    try:
        while True:
            n, k = list(map(int, input().split()))
            time = 240 - k
            result = 0
            for i in range(1, n + 1):
                if time < 5 * i:
                    break
                time -= 5 * i
                result += 1

            print(result)

    except EOFError:
        pass


main()
