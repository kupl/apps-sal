N = int(input())
A = list(map(int, input().split()))
set_A = list(set(A))

if len(set_A) == N:
    print("YES")
else:
    print("NO")
