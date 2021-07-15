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
    n= int(input())
    a = [int(x) for x in input().split()]
    
    dd = set(a)
    print(len(dd) - 1 if 0 in dd else len(dd))

    
def __starting_point():
    main()

__starting_point()
