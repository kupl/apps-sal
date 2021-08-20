print('97 97')
(A, B) = map(int, input().split())
if A > B:
    char = ['.', '#']
    M = A
    m = B
else:
    char = ['#', '.']
    M = B
    m = A
for i in range(1, 98):
    str = ''
    for j in range(1, 98):
        if i % 4 == 1 or j % 4 == 1:
            str += char[1]
        elif M < (i - 1) // 4 * 24 + (j - 1) // 4 + 1:
            str += char[1]
        elif i % 4 == j % 4 == 3 and m > (i - 1) // 4 * 24 + (j - 1) // 4 + 1:
            str += char[1]
        else:
            str += char[0]
    print(str)
