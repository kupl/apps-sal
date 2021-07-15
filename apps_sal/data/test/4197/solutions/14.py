import numpy

N = int(input())
A_list = list(map(int, input().split()))

ans_list = numpy.argsort(A_list)
for i in range(N):
    ans_list[i] += 1
print(*ans_list)
