T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    if all(l % 2 == L[0] % 2 for l in L):
        print("YES")
    else:
        print("NO")
