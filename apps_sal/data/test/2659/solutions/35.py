K = int(input())

def S(n):
    return sum(int(c) for c in str(n))
d9 = 0
cnt = 0
upper = 1
while cnt < K:
    n = int(str(upper) + ('9' * d9))
    if n <= S(n) * (10 ** d9):
        print(n)
        cnt += 1
        upper += 1
    else:
        d9 += 1
        upper //= 10

