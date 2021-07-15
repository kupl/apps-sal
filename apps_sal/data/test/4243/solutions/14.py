X = int(input())
y = X % 500

answer = (X // 500 * 1000 + y // 5 * 5)
print(answer)
