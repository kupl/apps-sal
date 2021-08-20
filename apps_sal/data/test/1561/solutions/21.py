"""This one should be very simple"""


def method(matrix, k):
    if k == 1:
        res = sum((line.count('.') for line in matrix))
    else:
        res = 0
        for is_transpose in (False, True):
            if is_transpose or len(matrix[0]) >= k:
                for line in matrix:
                    gen = iter(line)
                    consecutive = 0
                    for c in gen:
                        if c == '.':
                            consecutive += 1
                        else:
                            if consecutive >= k:
                                res += consecutive - k + 1
                            consecutive = 0
                            try:
                                while next(gen) == '*':
                                    pass
                                consecutive = 1
                            except StopIteration:
                                pass
                    if consecutive >= k:
                        res += consecutive - k + 1
            if not is_transpose:
                if len(matrix) < k:
                    break
                matrix = list(zip(*matrix))
    return res


(n, m, k) = list(map(int, input().split()))
matrix = []
for _ in range(n):
    matrix.append(input())
print(method(matrix, k))
