import re


def main():
    try:
        while True:
            n = int(input())
            p = list(map(int, input().split()))
            result = 'YES'
            for x in p:
                if len(re.findall('[aeiouy]', input())) != x:
                    result = 'NO'
            print(result)
    except EOFError:
        pass


main()
