(A, B) = list(map(int, input().split()))


def ans090(A: int, B: int):
    ans_count = 0
    for i in range(A, B + 1):
        if str(i) == str(i)[::-1]:
            ans_count += 1
    return ans_count


print(ans090(A, B))
