n, k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

arr.sort()

dif = [0] * n

for i in range(n - 1):
    dif[i] = arr[i + 1] - arr[i]

i = 0
j = n - 2
left = 1
right = 1

last = -1

while(k > 0 and i <= j):
    if(dif[i]) == 0:
        left += 1
        i += 1
        continue
    if(dif[j]) == 0:
        right += 1
        j -= 1
        continue

    if(i == j):
        last = i

    if(left <= right):
        difToSubstract = min(dif[i], k // left)

        if(difToSubstract == 0):
            k = 0
            break

        k -= left * difToSubstract
        dif[i] -= difToSubstract
    else:
        difToSubstract = min(dif[j], k // right)

        if(difToSubstract == 0):
            k = 0
            break

        k -= right * difToSubstract
        dif[j] -= difToSubstract

if(i <= j):
    sol = 0

    for u in range(i, j + 1):
        sol += dif[u]

    print(sol)

else:
    print(dif[last])
