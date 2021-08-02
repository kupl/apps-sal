n = int(input())
w = list(map(int, input().split()))


def answer(n: int, w: list) -> int:
    answer = sum(w)
    for i in range(len(w)):
        answer = min(answer, abs(sum(w[:i]) - sum(w[i:])))
    return answer


print(answer(n, w))
