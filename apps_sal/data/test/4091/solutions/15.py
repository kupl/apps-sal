(n, k) = map(int, input().split())
data = list(map(int, input().split()))
an_data = [(data[i], i) for i in range(n)]
an_data.sort(key=lambda x: x[0])
an_data = an_data[::-1]
ans = 0
answer = []
for i in range(k):
    ans += an_data[i][0]
    answer.append(an_data[i][1])
print(ans)
prev = 0
answer.sort()
for i in range(k):
    el = answer[i]
    if i == k - 1:
        print(n - prev)
        break
    if prev == 0:
        print(el + 1, end=' ')
        prev = el + 1
        continue
    print(el - prev + 1, end=' ')
    prev = el + 1
