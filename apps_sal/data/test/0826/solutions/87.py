n = int(input())

def check(k):
    return  k*(k + 1) // 2<= n + 1#条件をここに書く
 
left = 0                   # True
right = 10 ** 18 + 1      # False

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print((n - left + 1))

