(n, r, avg) = list(map(int, input().split()))
array = []
s = 0
for index in range(0, n):
    array.append(list(map(int, input().split())))
    s += array[index][0]
array.sort(key=lambda x: x[1])
index = 0
answer = 0
while s // n < avg:
    if s + r - array[index][0] >= avg * n:
        answer += array[index][1] * (avg * n - s)
        break
    s += r - array[index][0]
    answer += array[index][1] * (r - array[index][0])
    index += 1
print(answer)
