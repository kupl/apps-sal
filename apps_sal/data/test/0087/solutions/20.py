m, first_day = list(map(int, input().split()))
year = [31,28,31,30,31,30,31,31,30,31,30,31]
days_num = year[m-1]
left = days_num - (7 - first_day + 1)
if(left % 7 == 0):
    print(1 + left//7)
else:
    print(2 + left//7)

