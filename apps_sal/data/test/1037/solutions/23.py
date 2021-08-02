#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import functools
import heapq
import itertools
import logging
import math
import random
import string
import sys
from argparse import ArgumentParser
from collections import defaultdict, deque
from copy import deepcopy
from typing import Dict, List, Optional, Set, Tuple


def solve(values: List[int], nb: int) -> int:
    s_values = sorted(((v, i) for i, v in enumerate(values)), reverse=True)
    dp = [[0 for _ in range(nb + 1)] for _ in range(nb + 1)]
    for i, (v, p) in enumerate(s_values, start=1):
        for x in range(i + 1):
            y = i - x
            if y == 0:
                dp[x][y] = dp[x - 1][0] + abs(p - x + 1) * v
                continue
            if x == 0:
                dp[x][y] = dp[x][y - 1] + abs(nb - y - p) * v
                continue
            dp[x][y] = max(
                dp[x - 1][y] + abs(p - x + 1) * v, dp[x][y - 1] + abs(nb - y - p) * v
            )
    return max(dp[i][nb - i] for i in range(nb + 1))


def do_job():
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N = int(input())
    values = list(map(int, input().split()))
    # values = []
    # for _ in range(N):
    #     values.append(input().split())
    result = solve(values, N)
    print(result)


def print_output(testcase: int, result) -> None:
    "Formats and print result"
    if result is None:
        result = "IMPOSSIBLE"
    print(("Case #{}: {}".format(testcase + 1, result)))
    # 6 digits float precision {:.6f} (6 is the default value)
    # print("Case #{}: {:f}".format(testcase + 1, result))


def configure_log(log_file: Optional[str] = None) -> None:
    "Configure the log output"
    log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s:%(lineno)d - " "%(levelname)s - %(message)s"
    )
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    LOG.addHandler(handler)


LOG = None
# for interactive call: do not add multiple times the handler
if not LOG:
    LOG = logging.getLogger("template")
    configure_log()


def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="run as verbose mode",
    )
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.DEBUG)
    do_job()
    return 0


def __starting_point():
    import doctest

    doctest.testmod()
    return(main())


class memoized:
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


__starting_point()
