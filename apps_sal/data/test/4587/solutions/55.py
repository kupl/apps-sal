N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()


def bin_serch(array, num):
    head = 0
    tail = len(array)
    while head < tail:
        center = (head + tail) // 2
        if num < array[center]:
            tail = center
        else:
            head = center + 1
    return head


BC = [0 for _ in range(len(B))]
for i in range(len(B)):
    BC[i] = len(C) - bin_serch(C, B[i])
s = 0
for i in range(len(BC) - 1, -1, -1):
    s += BC[i]
    BC[i] = s
ans = 0
for a in A:
    b = bin_serch(B, a)
    if b < len(B):
        ans += BC[b]
print(ans)
