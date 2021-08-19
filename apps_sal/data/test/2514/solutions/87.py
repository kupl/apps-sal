from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
# BC=[]
# for i in range(Q):
#    BC.append(list(map(int,input().split())))
A_sum = sum(A)
A_count = Counter(A)

for i in range(Q):
    B, C = (map(int, input().split()))
    A_sum += (C - B) * A_count[B]
    A_count[C] += A_count[B]
    A_count[B] = 0
    print(A_sum)
