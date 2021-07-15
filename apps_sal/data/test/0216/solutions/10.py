n = int(input())
L = list(map(int, input().split()))
L = list(map(abs, L))
print(sum(L))

