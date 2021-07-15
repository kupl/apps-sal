N = int(input())
B = list(map(int, input().split()))

cnt = 0
for i in range(len(B)-1):
    cnt += min(B[i],B[i+1])

#端点
cnt += (B[0]+B[N-2])
print(cnt)
