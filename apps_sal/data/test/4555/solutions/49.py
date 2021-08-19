from typing import List


def answer(a: int, b: int, k: int) -> List[int]:
    a_k = set(range(a, min(a + k, b + 1)))
    k_b = set(range(max(b - k + 1, a + 1), b + 1))
    return sorted(a_k.union(k_b))


def main():
    (a, b, k) = list(map(int, input().split()))
    for i in answer(a, b, k):
        print(i)


def __starting_point():
    main()


__starting_point()
