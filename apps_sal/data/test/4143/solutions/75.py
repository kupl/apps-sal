n = int(input())
capa = [int(input()) for _ in range(5)]
min_capa = min(capa)
if min_capa >= n:
    print(5)
elif n % min_capa == 0:
    print(5 + n // min_capa - 1)
else:
    print(5 + n // min_capa)
