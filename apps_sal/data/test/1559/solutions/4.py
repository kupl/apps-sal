n = int(input())
A = input()
L = len(A)


def check_increase(p_numb, n):
    if p_numb.count('9') == n:
        return True
    return False


def large_print(L, n):
    cycle_count = L // n + 1
    p_numb = '1' + '0' * (n - 1)
    print(p_numb * cycle_count)


if L == n:
    if check_increase(A[:n], n):
        large_print(L, n)
    else:
        print(int(A) + 1)
elif L % n == 0:
    p_numb = A[:n]
    for i in range(n, L):
        if int(p_numb[i % n]) > int(A[i]):
            break
        elif int(p_numb[i % n]) < int(A[i]):
            p_numb = str(int(p_numb) + 1)
            break
    else:
        p_numb = str(int(p_numb) + 1)
    if len(p_numb) == n:
        print(p_numb * (L // n))
    else:
        large_print(L, n)
else:
    large_print(L, n)
