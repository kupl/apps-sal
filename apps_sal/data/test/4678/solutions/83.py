
def main(A):
    ans = 0
    max_num = A[0]
    for a in A:
        max_num = max(max_num, a)
        ans += max_num - a

    return ans

def __starting_point():
    N = int(input())
    A = list(map(int, input().split()))
    ans = main(A)
    print(ans)


__starting_point()
