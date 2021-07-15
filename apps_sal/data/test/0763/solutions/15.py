
import sys
def __starting_point():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    sum1 = 0
    for i in range(len(a)):
        sum1+=a[i]*i*2
    print(sum1*2)
__starting_point()
