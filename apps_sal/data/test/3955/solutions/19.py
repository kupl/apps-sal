import sys
class IoTool:  # a tool for input redirection 
    DEBUG = 0
    def _reader_dbg():
        with open('./input.txt', 'r') as f:
            lines = f.readlines()
        for l in lines: yield l.strip() 
    def _reader_oj():  
        return iter(sys.stdin.read().split('\n'))
    reader = _reader_dbg() if DEBUG else _reader_oj()
    def read(): return next(IoTool.reader)

input = IoTool.read

def main():
    n, k, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mul = 1
    for i in range(k): mul *= x
    if n == 1:
        print(a[0] * mul)
        return
    pre, tail = [0] * n, [0] * n
    pre[0] = a[0]
    tail[n-1] = a[n-1]
    
    for i in range(1, n): pre[i] = pre[i-1] | a[i]
    for i in range(n-2, -1, -1): tail[i] = tail[i+1] | a[i]
    answer = max((pre[0]*mul) | tail[1], pre[n-2]|(tail[n-1]*mul))
    for i in range(1, n-1):
        answer = max(answer, (a[i] * mul) | pre[i-1] | tail[i+1])
    print(answer)


def __starting_point():
    main()

__starting_point()
