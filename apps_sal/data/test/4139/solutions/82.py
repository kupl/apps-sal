import sys

N = int(input())
sys.setrecursionlimit(27000)

cnt = 0


def func(n: int, x: str):
    nonlocal cnt
    cnt_3 = x.count('3')
    cnt_5 = x.count('5')
    cnt_7 = x.count('7')
    if n < len(x):
        return 0
    if int(x) <= N and cnt_3 > 0 and cnt_5 > 0 and cnt_7 > 0:
        cnt += 1
    func(n, x + '3')
    func(n, x + '5')
    func(n, x + '7')


func(len(str(N)), '3')
func(len(str(N)), '5')
func(len(str(N)), '7')
print(cnt)
