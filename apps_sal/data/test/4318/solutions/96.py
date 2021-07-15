n = int(input())
h = list(map(int, input().split()))

def answer(n: int, h: list) -> int:
    h_list = 0
    answer = 0
    for i in h:
        if h_list <= i:
            answer += 1
        h_list = max(h_list, i)
    return answer

print(answer(n, h))
