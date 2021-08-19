def keisan(N, A):
    KAI = 0
    A.sort
    min = -100
    max = 101
    i = min
    while i <= max:
        kari = 0
        j = 0
        while j < N:
            kari += (A[j] - i) ** 2
            j += 1
        if kari <= KAI or i == min:
            KAI = kari
        i += 1
    return KAI


N = int(input())
A = input().split()
int_list = list(map(int, A))
print(keisan(N, int_list))
