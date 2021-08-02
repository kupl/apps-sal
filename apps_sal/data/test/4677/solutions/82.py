# https://atcoder.jp/contests/abc043/tasks/abc043_b

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
    if operation == "0":
        # 右端に0を追加
        q.append("0")

    elif operation == "1":
        # 右端に1を追加
        q.append("1")

    elif operation == "B":
        # バックスペース
        # 右端を一つ削除
        # q の中身が空でもエラーにならないように例外処理
        try:
            q.pop()
        except IndexError:
            pass  # 何もしない

# キューの中身を順番に取り出して文字列に変換
answer = ""
for i in q:
    answer = answer + i

print(answer)
