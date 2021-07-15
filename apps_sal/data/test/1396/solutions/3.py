def can_destroy(A):
    color_now = A[0]
    num_now = 1
    for i in range(1, len(A)):
        if color_now == A[i]:
            num_now += 1
            if num_now == 3:
                return i - 2
        else:
            color_now = A[i]
            num_now = 1
    return -1
        

def destroy(A):
    while len(A) > 0 and can_destroy(A) != -1:
        i = can_destroy(A)
        c = A[i]
        while i < len(A) and A[i] == c:
            A.pop(i)
    return A

n, k, x = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for i in range(len(A) + 1):
    B = A[:]
    B.insert(i, x)
    B = destroy(B)[:]
    res = max(res, len(A) - len(B))
print(res)
