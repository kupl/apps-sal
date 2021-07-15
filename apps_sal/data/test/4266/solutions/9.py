k, x = list(map(int, input().split()))

answer = []
for i in range((x - (k - 1)), (x + k)):
    answer.append(i)


print((" ".join(map(str, answer))))

