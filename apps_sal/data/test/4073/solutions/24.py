size = int(input())
a = [int(i) for i in input().split()]
print(max(a) ^ a[-1])
