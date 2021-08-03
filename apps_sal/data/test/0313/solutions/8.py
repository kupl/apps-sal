import sys
import re
sys.stdin.readline()
s = sys.stdin.readline()
s = re.sub('[^01]', '', s)
s = s.strip('0')
s = re.sub('0{2,}', '', s)
# print(repr(s))
print(len(s))
