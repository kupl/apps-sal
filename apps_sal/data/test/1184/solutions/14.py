import sys


def main(stdin):
    return len(set([e for e in stdin[0][1:-1].split(', ') if e != '']))


def __starting_point():
    skip_first_line = False
    stdin = [ln for ln in [ln.rstrip() for ln in sys.stdin.readlines()[1 if skip_first_line else 0:]] if len(ln) > 0]
    print(main(stdin))

__starting_point()
