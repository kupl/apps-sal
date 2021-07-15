import sys
input = sys.stdin.readline

t=int(input())
for testcases in range(t):
    n=int(input())

    ANS=[n//1]

    for i in range(2,n):
        ANS.append(n//i)

        if n/(i-1)-n/i<1:
            break

    A=list(range(0,ANS[-1]))+sorted(set(ANS))

    print(len(A))
    print(*A)

