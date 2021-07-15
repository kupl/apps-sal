mm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
m, d = list(map(int, input().split()))
print((mm[m-1]+d-2)//7+1)

