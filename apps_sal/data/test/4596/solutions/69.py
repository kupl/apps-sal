# coding: utf-8
# Your code here!

def divided_2(x): return int(x / 2)
def enable_divided_2(x): return True if int(x % 2) == 0 else False


n = int(input())
A = list(map(int, input().split()))
cnt = 0

while(1):
    if False in list(map(enable_divided_2, A)):
        break
    A = list(map(divided_2, A))
    cnt += 1

print(cnt)
