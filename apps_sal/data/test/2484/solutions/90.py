

def bin20(x):
    bin_x = bin(x)[2:]
    x_len = len(bin_x)

    return list(map(int, "0" * (20 - x_len) + bin_x))


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [bin20(a) for a in A]

    ans = 0
    left = 0
    right = 0
    sum20 = [0] * 20
    pre_right = -1
    while True:
        if right > pre_right:
            for k in range(20):
                sum20[k] += A[right][k]

        pre_right = right

        if 2 in sum20:
            for k in range(20):
                sum20[k] -= A[left][k]
            ans += right - left
            left += 1
        else:
            right += 1

        if right == N:
            ans += (N - left) * (N - left + 1) // 2

            return ans


print((main()))
