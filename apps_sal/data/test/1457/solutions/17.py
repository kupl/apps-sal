import sys
import re

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

print(len(re.findall(b, a)))

