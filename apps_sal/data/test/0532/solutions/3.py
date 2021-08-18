

def main():
    try:
        while True:
            s = input()
            cur = 0
            result = 0
            for c in s:
                c = ord(c) - 97
                result += min((c - cur) % 26, (cur - c) % 26)
                cur = c
            print(result)

    except EOFError:
        pass


main()
