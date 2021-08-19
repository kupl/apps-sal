(n, k) = map(int, input().split())
a = sorted(list(map(int, input().split())))
answer = 0
for elem in a:
    while 2 * k < elem:
        k *= 2
        answer += 1
    k = max(k, elem)
print(answer)
