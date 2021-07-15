N = int(input())
num = [[0] * 10 for i in range(10)]
for i in range(1, N + 1):
    num[int(str(i)[0])][int(str(i)[-1])] += 1
    
ans = 0
for i in range(1, N + 1):
    ans += num[int(str(i)[-1])][int(str(i)[0])]
print(ans)
