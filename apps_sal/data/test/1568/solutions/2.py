import atexit
import io
import sys

# Buffering IO
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    

def main():
    n, a, b, c, tt = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    
    s = a * n
    if c > b:
        for ti in t:
            s += (c-b) * (tt-ti)
    print(s)
            

    
def __starting_point():
    main()

__starting_point()
