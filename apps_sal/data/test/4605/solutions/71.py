# coding: utf-8
# Your code here!

def sumDigit(x):
  sum_ = 0
  while x > 0:
    sum_ += x%10
    x //= 10
  return sum_

N,A,B=(int(x) for x in input().split())

ss = 0
for i in range(N):
  num = sumDigit(i+1)
  if num >= A and num <= B:
    ss += i+1

print(ss)
