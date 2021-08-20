import sys
sys.stdin.readline()
ar = [int(c) for c in sys.stdin.readline().split(' ')]
n = len(ar)
calcd = [a // max(i, n - i - 1) for (i, a) in enumerate(ar)]
sys.stdout.write(f'{min(calcd)}\n')
