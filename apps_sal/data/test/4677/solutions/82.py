"""
双方向キューをつかって実装する

このどれかの操作ができる
* 0 をキューに入れる
* 1 をキューに入れる
* キューの最後のものを出す

注意: キューが空の場合にバックスペースをしても何も起きないようにする
"""
from collections import deque
q = deque()
s = input()
for operation in s:
    if operation == '0':
        q.append('0')
    elif operation == '1':
        q.append('1')
    elif operation == 'B':
        try:
            q.pop()
        except IndexError:
            pass
answer = ''
for i in q:
    answer = answer + i
print(answer)
