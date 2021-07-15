import sys

A, B = map(int, sys.stdin.readline().split())

"""
..........
..........
..........
に、連結にならないように黒を置いていく
白の場合も白黒を逆にして同じことをやれば良い
"""
A -= 1
B -= 1
print(100, 100)
for i in range(100):
    for j in range(100):
        # 黒一面に白を入れていく
        if i < 50:
            if A > 0 and i % 2 == 0 and j % 2 == 0:
                print(".", end="")
                A -= 1
            else:
                print("#", end="")
        # 白一面に黒を入れていく
        elif 50 <= i:
            if B > 0 and i % 2 == 1 and j % 2 == 0:
                print("#", end="")
                B -= 1
            else:
                print(".", end="")
        if j == 99:
            print("")
