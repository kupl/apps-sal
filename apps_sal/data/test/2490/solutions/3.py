S = input()[::-1]
ans = 0
# 支払う枚数
array = list(map(int, S))
L = len(array)
for i, n in enumerate(array):
    if n < 5:
        ans += n
    elif n > 5:
        ans += 10 - n
        if i < L - 1:
            array[i + 1] += 1
        else:
            ans += 1
    else:
        ans += 5
        if i < L - 1:
            if array[i + 1] >= 5:
                array[i + 1] += 1

print(ans)
