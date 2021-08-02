K = int(input())
A, B = list(map(int, input().split()))
for x in range(A, B + 1):
    if x % K == 0:
        print("OK")
        break
else:
    print("NG")
