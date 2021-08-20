import sys
r_input = sys.stdin.readline
n = int(r_input())
s = r_input().rstrip()
print(s.count('L') + s.count('R') + 1)
