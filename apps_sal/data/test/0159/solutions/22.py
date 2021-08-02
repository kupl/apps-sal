from math import sqrt
n = int(input())
a = [int(i) for i in input().split()]
insert = [0] * n
ans = []
cnt = 0


def is_co_prime(A, B):
    t = A % B
    if t == 0:
        return B == 1, B
    while True:
        A, B = B, t
        if A % B:
            t = A % B
        else:
            C = B
            break
    return C == 1, C


for i in range(n - 1):
    check = is_co_prime(a[i], a[i + 1])
    if check[0]: continue
    else:
        T = int(sqrt(check[1]))
        while True:
            if is_co_prime(a[i], T)[0] and is_co_prime(T, a[i + 1])[0]:
                break
            T += 1
        insert[i] = T
        cnt += 1

for i in range(n):
    ans.append(a[i])
    if insert[i]:
        ans.append(insert[i])

print(cnt)
print(" ".join(map(str, ans)))
