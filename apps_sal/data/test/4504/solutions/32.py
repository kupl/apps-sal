S = list(input())


def judge(A):
    if len(A) % 2 == 0:
        if A[:len(A) // 2] == A[len(A) // 2:]:
            return True
    return False


for i in range(len(S)):
    S.pop()
    if judge(S):
        break
print(len(S))
