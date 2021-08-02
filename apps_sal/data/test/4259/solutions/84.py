K = int(input())
A, B = map(int, input().split())
if (B % K == 0) or (A % K == 0) or (B // K != A // K):
    print("OK")
else:
    print("NG")
