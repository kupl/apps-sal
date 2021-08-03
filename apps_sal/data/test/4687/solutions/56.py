import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    A = [0 for i in range(10 ** 5 + 1)]
    for i in range(n):
        a, b = map(int, input().split())
        A[a] += b

    i = 0
    sum = 0
    while(sum < k):
        i += 1
        sum += A[i]
    print(i)


main()
