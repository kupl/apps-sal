K = int(input())
A, B = list(map(int, input().split()))

if A % K == 0 or B % K == 0:
    print("OK")
else:
    if A // K == B // K:
        print("NG")
    else:
        print("OK")

