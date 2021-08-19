n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
# 縦軸の和、横軸の和を求めて、掛け合わせる。

# listから、和を求める


def calc(lis):
    num = len(lis)
    sum = 0
    for i in range(num):
        #sum += x[i] * (num - i - 1) - x[i] * (i)
        sum += lis[i] * i - (lis[i] * (num - i - 1))

    return sum
    '''
          lisSum = 0
          before = 0
          for i, val in enumerate(lis):
              lisSum += val
              if (i != 0):
                  temp = before + val
                  lisSum = temp
              before = val

          return int(lisSum)

      '''


xSum = calc(x)
ySum = calc(y)

ans = (xSum * ySum) % MOD
print(ans)


'''
def calc(list):

sum = 0
for i in range(n):
  temp = n - i
  for j in range(i+1, n):
    sum += list[i] - list[j]

二重ループにせずとも、
for i in range(n):
  sum += x[i]*(n-i-1) - x[1]*(i)

でOK
'''
