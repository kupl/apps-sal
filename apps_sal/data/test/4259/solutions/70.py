K = int(input())
A,B = list(map(int,input().split()))

if (A // K) ==  (B // K) and (A % K) != 0:
    print("NG")

else:
    print("OK")

