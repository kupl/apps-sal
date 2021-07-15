def operate(S,A,B,C,N):
    OP = []
    for i in range(N):
        if S[i] == "AB":
            if A == 0 and B == 0:
                return -1
            else:
                if A == 1 and B == 1 and i < N-1:
                    if S[i+1] == "BC":
                        OP.append("B")
                        A,B = A-1,B+1
                    else:
                        OP.append("A")
                        A,B = A+1,B-1
                elif A >= B:
                    OP.append("B")
                    A,B = A-1,B+1
                else:
                    OP.append("A")
                    A,B = A+1,B-1
        if S[i] == "BC":
            if B == 0 and C == 0:
                return -1
            else:
                if B == 1 and C == 1 and i < N-1:
                    if S[i+1] == "AB":
                        OP.append("B")
                        B,C = B+1,C-1
                    else:
                        OP.append("C")
                        B,C = B-1,C+1
                elif B >= C:
                    OP.append("C")
                    B,C = B-1,C+1
                else:
                    OP.append("B")
                    B,C = B+1,C-1
        if S[i] == "AC":
            if A == 0 and C == 0:
                return -1
            else:
                if A == 1 and C == 1 and i < N-1:
                    if S[i+1] == "BC":
                        OP.append("C")
                        A,C = A-1,C+1
                    else:
                        OP.append("A")
                        A,C = A+1,C-1
                elif C >= A:
                    OP.append("A")
                    C,A = C-1,A+1
                else:
                    OP.append("C")
                    C,A = C+1,A-1
    return OP

def main():
    N,A,B,C = list(map(int,input().split()))
    S = [input() for _ in range(N)]

    ans = operate(S,A,B,C,N)
    if ans != -1:
        print("Yes")
        for i in range(N):
            print((ans[i]))
    else:
        print("No")

def __starting_point():
    main()

__starting_point()
