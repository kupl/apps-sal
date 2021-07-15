argList = list(map(int, input().split()))
k = int(input())
print((sum(argList)-max(argList)) + max(argList)*2**k)
