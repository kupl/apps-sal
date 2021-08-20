import sys
if sys.platform == 'ios':
    sys.stdin = open('input_file.txt')
x = int(input())
k = x // 11
if x == 11 * k:
    ans = 2 * k
elif 11 * k < x and x <= 11 * k + 6:
    ans = 2 * k + 1
else:
    ans = 2 * (k + 1)
print(ans)
