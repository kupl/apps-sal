N = int(input())
bs = list(map(int, input().split()))
list_a = [bs[0]]
for i in range(1, len(bs)):
    a = min(bs[i - 1], bs[i])
    list_a.append(a)
list_a.append(bs[len(bs) - 1])
print(sum(list_a))
