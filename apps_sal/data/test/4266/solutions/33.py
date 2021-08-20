(K, X) = map(int, input().split())
num = []
for i in range(X - (K - 1), X + (K - 1) + 1):
    num.append(i)
num = [str(a) for a in num]
answer = ' '.join(num)
print(answer)
