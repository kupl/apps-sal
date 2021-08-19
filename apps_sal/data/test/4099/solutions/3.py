n, k, m = map(int, input().split())
a = map(int, input().split())

score = sum(a)

for i in range(k + 1):  # iは最後のテストの点数、0から増やしていく。満点kの時まで繰り返すためにk+1
    total = score + i
    avarage = total / n
#    print(i,'total',total,'avarage',avarage)
    if avarage >= m:
        print(i)
        break
    if i == k:
        print('-1')
