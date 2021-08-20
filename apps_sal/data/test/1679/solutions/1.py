import sys
input = sys.stdin.readline
num = ''
cnt = 0
input()
for ch in input().strip() + '0':
    if ch == '1':
        cnt += 1
    else:
        num += str(cnt)
        cnt = 0
print(num)
