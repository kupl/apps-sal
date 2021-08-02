n = int(input())
a = [int(i) for i in input().split()]
answer = [0] * n
answer[0] = 1

for i in range(1, n):
    if a[i] == 1:
        answer[i] = max(answer) + 1
    else:
        temp_max = 0
        for j in range(i):
            if a[j] == 0 and answer[j] > temp_max:
                temp_max = answer[j]
        answer[i] = temp_max + 1

print(max(answer))
