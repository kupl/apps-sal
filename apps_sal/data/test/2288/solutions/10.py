T = int(input())
for t in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = sum(b)
    if s != 0 and s != n:
        print("Yes")
    else:
        if sorted(A) == A:
            print("Yes")
        else:
            print("No")

