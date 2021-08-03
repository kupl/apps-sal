# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
x = [0, 4, 6, 8, 8, 9, 10, 11, 11, 13]

n = int(input())
ret = 1 if n == 0 else 0
while n:
    ret += x.count(n - (n // 16) * 16)
    n = n // 16
print(ret)
