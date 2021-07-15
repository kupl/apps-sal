n = int(input())
arr = list(map(int, input().split()))
c0 = arr.count(0)
c5 = n - c0
if c5 >= 9 and c0 > 0:
    str = ((c5//9) * 9) * '5'
    str += c0 * '0'
elif c0 >= 1:
    str = '0'
else:
    str = '-1'
print(str)

