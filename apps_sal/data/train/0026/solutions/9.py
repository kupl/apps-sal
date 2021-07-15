import sys
ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)

def main():
    ntc = next(ints)
    for tc in range(ntc):
        n, m = (next(ints) for i in range(2))
        print('YES' if n==1 or m==1 or n==m==2 else 'NO')
    return

main()

