__author__ = 'trunghieu11'

def calc(n, h1, h2, w1, w2):
    answer = 0
    len = n // w1
    for i in range(0, min(len, 100000) + 1):
        answer = max(answer, i * h1 + (n - i * w1) // w2 * h2)
    return answer

n, hR, hB, wR, wB = map(int, input().split())
print(max(calc(n, hR, hB, wR, wB), calc(n, hB, hR, wB, wR)))
