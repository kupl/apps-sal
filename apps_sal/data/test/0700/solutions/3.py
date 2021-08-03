def solve(board):
    n = len(board)
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] is 'X':
                ans += 2**(i * n + j)
    return ans


def reverse_array(arr):
    for i in range(len(arr)):
        arr[i].reverse()


def rotate(matrix, degree):
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(zip(*matrix[::-1]), degree - 90)
    else:
        return rotate(zip(*matrix)[::-1], degree + 90)


def make_list(board):
    board = list(board)
    arr = []
    for i in range(len(list(board))):
        arr.append(list(board[i]))
    return arr


def add_rotations(board, st):
    for i in range(4):
        st.add(solve(board))
        reverse_array(board)
        st.add(solve(board))
        reverse_array(board)
        board = make_list(rotate(board, 90))


n = int(input())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(input().strip()))
for _ in range(n):
    arr2.append(list(input().strip()))
s = set()
s.add(solve(arr1))
add_rotations(arr1, s)
l1 = len(s)
# print(s,arr1,arr2)
s.add(solve(arr2))
add_rotations(arr2, s)
# print(s)
l2 = len(s)
if l1 == l2:
    print("Yes")
else:
    print("No")
