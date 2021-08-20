def main():
    N = int(input())
    A = [int(a) for a in input().split(' ')]
    if A.count(0) > 0:
        print(sum([abs(a) for a in A]))
        return 0
    minus = 0
    for i in range(len(A)):
        if A[i] < 0:
            minus += 1
    if minus % 2 == 0:
        print(sum([abs(a) for a in A]))
        return 0
    A.sort(key=lambda a: abs(a))
    print(sum([abs(a) for a in A[1:]]) - abs(A[0]))


main()
