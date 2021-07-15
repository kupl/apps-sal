from collections import Counter
import sys
ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)

def main():
    n = next(ints)
    A = [0]*n
    for i in range(n): A[next(ints)-1]=i
    b = [next(ints) for i in range(n)]
    ans = max(Counter((i-A[b[i]-1])%n for i in range(n)).values())
    print(ans)
    return

main()

