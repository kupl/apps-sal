def atc_080a(NAB: str) -> int:
    (N, A, B) = list(map(int, NAB.split(' ')))
    return min(N * A, B)


NAB = input()
print(atc_080a(NAB))
