def main():
    N = int(input())
    A = [int(a) for a in input().split(" ")]
    A.sort()

    if N % 2 == 1 and A.count(0) != 1:
        print(0)
        return 0
    elif N % 2 == 0 and A.count(0) > 0:
        print(0)
        return 0

    if N % 2 == 1:
        A.pop(0)

    cnt = 0
    while len(A) > 0:
        if A[0] != A[1] or (len(A) > 2 and A[0] == A[1] and A[1] == A[2]):
            print(0)
            return 0
        elif A[0] == A[1] == 2 * cnt + (N % 2) + 1:
            cnt += 1
            A.pop(0)
            A.pop(0)
        else:
            print(0)
            return 0

    ans = 1
    for p in range(cnt):
        ans = (ans * 2) % 1000000007
    print(ans)


main()
