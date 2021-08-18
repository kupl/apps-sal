
a = int(input())
s = input()

if a < 2800 or 5000 <= a:
    print('数値が範囲外です')
if len(s) < 1 or 10 < len(s):
    print('文字数が範囲外です')
elif a < 3200:
    print('red')
else:
    print(s)
