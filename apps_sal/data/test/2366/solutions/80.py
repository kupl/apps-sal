""" スニペット """
import math


def get_int():
    return int(input())


def get_ints():
    return list(map(int, input().split()))


' スニペット '


def choose2(n):
    return n * (n - 1) // 2


N = get_int()
An = get_ints()
' 全ての要素から2つのボールを選ぶ通り数を求める '
uni = [0] * (N + 1)
for i in range(N):
    uni[An[i]] += 1
sumWay = 0
con = [0] * (N + 1)
for i in range(N + 1):
    con[i] = choose2(i)
'\nfor i in range(N + 1):\n    sumWay += con(uni[i])\n'
for i in uni:
    sumWay += con[i]
' 全ての要素数 - 削除する要素の通り数 + 削除する要素を引いた際の通り数 を求める '
for i in range(N):
    print(sumWay - con[uni[An[i]]] + con[uni[An[i]] - 1])
