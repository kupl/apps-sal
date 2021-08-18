import sys
read = sys.stdin.read
readline = sys.stdin.readline


s = input()

if ((s[0] == s[-1]) + len(s)) & 1:
    print("First")
else:
    print("Second")
