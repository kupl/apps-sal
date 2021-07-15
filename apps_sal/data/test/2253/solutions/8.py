import sys
r_input = sys.stdin.readline

t = int(r_input())

for _ in range(t):
    s = r_input().rstrip()
    if s.endswith('po'):
        print('FILIPINO')
    elif s.endswith('desu') or s.endswith('masu'):
        print('JAPANESE')
    elif s.endswith('mnida'):
        print('KOREAN')
