n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] * n
t = 1
for i in A:
    C[i - 1] = t
    t += 1
t = 0
for i in B:
    if C[i - 1] > t:
        print(C[i - 1] - t, end = ' ')
        t = C[i - 1] 
    else:
        print(0, end = ' ')
print()
