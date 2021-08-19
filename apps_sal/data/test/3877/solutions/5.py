(n, l, r) = [int(x) for x in input().strip().split(' ')]


def handlerequest(n, l, r):
    if n == 0 or n == 1:
        return n if l == r else 0
    else:
        size = 2 ** (n.bit_length() - 1) - 1
        if r <= size:
            return handlerequest(n // 2, l, r)
        elif l > size + 1:
            return handlerequest(n // 2, l - size - 1, r - size - 1)
        else:
            return n % 2 + handlerequest(n // 2, l, size) + handlerequest(n // 2, 1, r - size - 1)


print(handlerequest(n, l, r))
