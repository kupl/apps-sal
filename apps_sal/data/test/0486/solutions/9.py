from collections import defaultdict
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

n = list(input())
c = 0
t = 1
for i in range(len(n)):
    j = int(n[i])
    t2 = t*(j-1)
    t = t*j
    c = max(t2*((9)**(len(n)-i-1)) , c)
    if i==0 and t2==0:
        c = max(((9)**(len(n)-i-1)) , c)
        
        
c = max(t,c)
print(c)
                

