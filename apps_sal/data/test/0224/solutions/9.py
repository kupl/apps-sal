from functools import reduce
from operator import add
import re


def main():
    try:
        while True:
            print(reduce(max, (len(m.group()) for m in re.finditer('[^AEIOUY]+', input())), 0) + 1)
    except EOFError:
        pass


main()
