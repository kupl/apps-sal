(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7


def calc(lis):
    num = len(lis)
    sum = 0
    for i in range(num):
        sum += lis[i] * i - lis[i] * (num - i - 1)
    return sum
    '\n          lisSum = 0\n          before = 0\n          for i, val in enumerate(lis):\n              lisSum += val\n              if (i != 0):\n                  temp = before + val\n                  lisSum = temp\n              before = val\n\n          return int(lisSum)\n\n      '


xSum = calc(x)
ySum = calc(y)
ans = xSum * ySum % MOD
print(ans)
'\ndef calc(list):\n\nsum = 0\nfor i in range(n):\n  temp = n - i\n  for j in range(i+1, n):\n    sum += list[i] - list[j]\n\n二重ループにせずとも、\nfor i in range(n):\n  sum += x[i]*(n-i-1) - x[1]*(i)\n\nでOK\n'
