import sys

r = lambda: sys.stdin.readline().rstrip()

def __starting_point():
    T = int(r())
    for _ in range(T):
        s = r()
        if s.endswith('po'): print('FILIPINO')
        elif s.endswith('desu') or s.endswith('masu'): print('JAPANESE')
        elif s.endswith('mnida'): print('KOREAN')

__starting_point()
