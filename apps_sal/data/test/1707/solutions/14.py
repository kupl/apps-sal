n = int(input())
a = sorted([int(x) for x in input().split()])
counter = 0
answer = 0
end = 1
for i in range(n):
    if a[i] < 0:
        a[i] = a[i] * (-1)
a.sort()
for i in range(n):
    end = max(end, i + 1)
    for j in range(end, n):
        if a[i] * 2 < a[j]:
            end = j
            break
        else:
            counter += 1
    else:
        end = j + 1
    answer += counter
    counter = max(counter - 1, 0)

print(answer)
