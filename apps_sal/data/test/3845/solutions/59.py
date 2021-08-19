import sys
(A, B) = map(int, sys.stdin.readline().split())
'\n..........\n..........\n..........\nに、連結にならないように黒を置いていく\n白の場合も白黒を逆にして同じことをやれば良い\n'
A -= 1
B -= 1
print(100, 100)
for i in range(100):
    for j in range(100):
        if i < 50:
            if A > 0 and i % 2 == 0 and (j % 2 == 0):
                print('.', end='')
                A -= 1
            else:
                print('#', end='')
        elif 50 <= i:
            if B > 0 and i % 2 == 1 and (j % 2 == 0):
                print('#', end='')
                B -= 1
            else:
                print('.', end='')
        if j == 99:
            print('')
