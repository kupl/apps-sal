def main():
    N = int(input())
    Q = 2 * N
    stack = []
    curr = 1
    ans = 0
    for _ in range(Q):
        A = input().strip().split(' ')
        if len(A) > 1:
            num = int(A[1])
            stack += [num]
        else:
            if stack != []:
                if stack[-1] == curr:
                    stack.pop()
                else:
                    ans += 1
                    stack = []
            curr += 1
    print(ans)


main()
