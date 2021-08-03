N = int(input())


def ans136(N):
    odd_count = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            odd_count += 1

    return odd_count


print((ans136(N)))
