def foo():
    n, m, k = list(map(int, input().split()))
    a, b = [0] * n, [0] * n
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
        b[a[i]] = i
    c = list(map(int, input().split()))
    answer = 0;
    for element in c:
        element -= 1
        answer += b[element] // k + 1
        if b[element]:
            a[b[element]], a[b[element] - 1] = a[b[element] - 1], a[b[element]]
            b[a[b[element]]] += 1
            b[element] -= 1
    return answer


print(foo())
