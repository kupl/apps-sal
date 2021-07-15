n = int(input())
A = list(map(int, input().split()))
Ka = 0
Cnt = 0
for i in range(n):
    Ka = max(Ka, A[i])
    if Ka <= i + 1:
        Cnt += 1
print(Cnt) 
