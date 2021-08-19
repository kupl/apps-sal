N, W = list(map(int, input().split()))
l = [input() for _ in range(N)]

print(('#' * (W + 2)))
for i in l:
    print(('#' + i + '#'))
print(('#' * (W + 2)))
