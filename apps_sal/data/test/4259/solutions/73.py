K = int(input())
[A, B] = [int(i) for i in input().split()]
for num in range(A, B+1):
    if num % K == 0:
        print("OK")
        return
print("NG")
