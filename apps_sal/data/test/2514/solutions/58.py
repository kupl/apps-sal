n = int(input())
sum = 0
a_list = list(map(int, input().split()))
num = [0] * (10 ** 5 + 1)
for i in range(n):
    num[a_list[i]] += 1
    sum += a_list[i]
q = int(input())
for i in range(q):
    (b, c) = map(int, input().split())
    sum += (c - b) * num[b]
    num[c] += num[b]
    num[b] = 0
    print(sum)
