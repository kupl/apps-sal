n = int(input())
a = list(map(int, input().split()))
q = int(input())
dic = [0 for _ in range(10 ** 5 + 1)]
count = 0
for i in a:
    dic[i] += 1
    count += i
for i in range(q):
    (b, c) = map(int, input().split())
    count -= b * dic[b]
    dic[c] += dic[b]
    count += c * dic[b]
    dic[b] = 0
    print(count)
