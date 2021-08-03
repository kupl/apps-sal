import sys
import logging
import math
from functools import reduce


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def lcm_list(numbers):
    return reduce(lcm, numbers)


def main():
    n = int(input())
    ans = lcm_list(list(range(2, n + 1)))
    print((ans + 1))


def __starting_point():
    if len(sys.argv) >= 2 and sys.argv[1] == "--debug":
        loglevel = "debug"
    else:
        loglevel = "warning"

    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)
    logging.basicConfig(
        level=numeric_level, format="%(levelname)s (%(asctime)s.%(msecs)d): %(message)s", datefmt="%I:%M:%S"
    )

    main()


__starting_point()
