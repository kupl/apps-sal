def read(type=int):
    return type(input())


def read_arr(type=int):
    return [type(token) for token in input().split()]


n = read()
S = [ord(c) - ord('1') for c in read(str)]
M = [ord(c) - ord('1') for c in read(str)]
self_knocks = 0
S.sort()
M.sort()
i = n - 1
j = n - 1
while i >= 0:
    if M[j] >= S[i]:
        j -= 1
        i -= 1
    else:
        self_knocks += 1
        i -= 1
op_knocks = 0
i = n - 1
j = n - 1
while i >= 0:
    if M[j] > S[i]:
        j -= 1
        i -= 1
        op_knocks += 1
    else:
        i -= 1
print(self_knocks)
print(op_knocks)
