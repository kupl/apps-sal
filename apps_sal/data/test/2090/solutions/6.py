
import heapq
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


def main():
    n, k = map(int, input().split())
    songs = []
    for _ in range(n):
        t, b = map(int, input().split())
        songs.append((b, t))
    songs.sort(reverse=True)

    ret = 0
    curr_count, curr_sum = 0, 0
    h = []
    for i in range(n):
        b, t = songs[i]
        heapq.heappush(h, t)
        curr_sum += t
        curr_count += 1
        if curr_count > k:
            curr_sum -= heapq.heappop(h)
            curr_count -= 1
        ret = max(ret, curr_sum * b)
    print(ret)


def __starting_point():
    main()


__starting_point()
