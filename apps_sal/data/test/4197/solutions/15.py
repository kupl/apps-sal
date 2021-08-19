N = int(input())
A = list(map(int, input().split()))
lis = [0] * N
k = 1
for i in A:
    lis[i - 1] = k
    k += 1
lis = map(str, lis)
ans = ' '.join(lis)
print(ans)
