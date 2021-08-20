(K, X) = list(map(int, input().split()))
min_value = X - K + 1
max_value = X + K
A = []
for i in range(min_value, max_value):
    i = str(i)
    A.append(i)
answer = ' '.join(A)
print(answer)
