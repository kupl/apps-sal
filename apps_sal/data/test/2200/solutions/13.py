__author__ = 'Lipen'

def main():
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))

    answer = list(map(lambda i: int( x[i] - (int(x[i] * a/b)) / a*b ), range(n)))

    print(' '.join(map(str, answer)))

main()
