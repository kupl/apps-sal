A, B = map(int, input().split())


def ans090(A: int, B: int):
    count = 0
    for i in range(A, B + 1):
        if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2]:
            count += 1
    return count


print(ans090(A, B))
