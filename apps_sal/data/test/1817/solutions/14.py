n = int(input())
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
T.sort()
if n%2==0:
    print(T[n//2-1])
else:
    print(T[n//2])

