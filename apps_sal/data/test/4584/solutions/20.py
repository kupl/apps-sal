def main():
    N = int(input())
    A = list(map(int, input().split()))
    list_a = [0] * N
    for i in range(len(A)):
        list_a[A[i] - 1] += 1
    for i in range(N):
        print(list_a[i])


main()
