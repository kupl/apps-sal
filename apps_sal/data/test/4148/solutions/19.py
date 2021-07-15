# 問題：https://atcoder.jp/contests/abc146/tasks/abc146_b

n = int(input())
s = input()

res = ''

for letter in s:
    res += chr(ord('A') + (ord(letter)-ord('A')+n) % 26)

print(res)

