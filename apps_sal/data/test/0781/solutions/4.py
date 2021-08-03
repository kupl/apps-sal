3


def readln(): return tuple(map(int, input().split()))


print('YES' if len([1 for _ in range(8) if input() in ['WB' * 4, 'BW' * 4]]) == 8 else 'NO')
