def main():

    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)
    Amax = A[-1]
    count = [0 for _ in range(Amax+1)]

    for a in A:
        for i in range(1, Amax//a+1):
            count[i*a] += 1

    ans = 0
    for i in range(N):
        a = A[i]
        if count[a] == 1:
#            print(i)                                                                                                                                            
            ans += 1

    print(ans)

def __starting_point():
    main()

__starting_point()
