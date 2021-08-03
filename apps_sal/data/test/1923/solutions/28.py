N = int(input())
L = list(map(int, input().split()))
print(sum(sorted(L)[0::2]))
