"""
1 2 3 4 5 6 ..... N(人)
        i = 身長:Ai(cm)

if A[i] > A[i+1]:
    A[i] == A[i+1] + 踏み台
"""


def step():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # 処理
    step_height_sum = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            step_height_sum += A[i] - A[i + 1]
            A[i + 1] = A[i]
    return step_height_sum


result = step()
print(result)
