import sys
import io

stream_enable = 0

inpstream = """
2 4
*.*.
1211
"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()

def inpmap():
    return list(map(int, input().split()))

n, m = inpmap()
arr = []
for i in range(n):
    arr.append(list(input()))
# print(arr)
for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":
            continue
        bomb = 0
        for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < n and 0 <= jj < m:
                bomb += arr[ii][jj] == "*"
        # print(i, j, bomb)
        if bomb == 0 and arr[i][j] == '.' or arr[i][j].isdigit() and int(arr[i][j]) == bomb:
            pass
        else:
            print("NO")
            return
print("YES")


