n = int(input())
count = 0
board = []
fail = False
while count < n:
    x = input()
    for letter in x:
        board.append(letter)
    count += 1
for i in range(n ** 2):
    total = 0
    if i - n < 0:
        pass
    elif board[i - n] == 'o':
        total += 1
    if i - 1 < 0:
        pass
    elif i % n == 0:
        pass
    elif board[i - 1] == 'o':
        total += 1
    if i + 1 > n ** 2 - 1:
        pass
    elif i % n == n - 1:
        pass
    elif board[i + 1] == 'o':
        total += 1
    if i + n > n ** 2 - 1:
        pass
    elif board[i + n] == 'o':
        total += 1
    if total % 2 == 1:
        fail = True
if fail == True:
    print('NO')
else:
    print('YES')
