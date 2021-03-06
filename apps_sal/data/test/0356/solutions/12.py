import atexit
import io
import sys
inf = float('inf')
inf_neg = float('-inf')
range_5 = int(100000.0 + 1)
range_6 = int(1000000.0 + 1)
range_7 = int(10000000.0 + 1)
range_8 = int(100000000.0 + 1)
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    if sum(a) != sum(b):
        print(-1)
    else:
        (i, j) = (0, 0)
        temp = 0
        while i < n or j < m:
            if a[i] == b[j]:
                temp += 1
                if i < n and j < m:
                    i += 1
                    j += 1
                else:
                    break
            elif a[i] < b[j] and i + 1 < n:
                a[i + 1] += a[i]
                i += 1
            elif a[i] < b[j] and i + 1 > n - 1:
                temp += 1
                break
            elif a[i] > b[j] and j + 1 < m:
                b[j + 1] += b[j]
                j += 1
            elif a[i] > b[j] and j + 1 > m - 1:
                temp += 1
                break
        print(temp)


def __starting_point():
    main()


__starting_point()
