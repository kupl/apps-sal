N = int(input())
B = list((int(x) for x in input().split()))
A1 = B + [100001]
A2 = [100001] + B
A = [min(A1[i], A2[i]) for i in range(N)]
print(sum(A))
