n, x, t = list(map(int,input().split()))

# result = 0
# 
# if n > x:
#     result += 1
# if n % x < x:
#     result += 1
# 
# print(result * t)


if n % x == 0:
    answer = (n//x*t)
else:
    answer = (n//x+1)*t
print((int(answer)))

