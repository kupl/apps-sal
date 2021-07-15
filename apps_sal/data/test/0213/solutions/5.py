n, m = list(map(int, input().split()))
#memory = [[] * 100 for i in range(100)]
memory = []
for i in range(m):
    a, b = list(map(int, input().split()))
    memory.append((a, b))
#memory.sort()
#count = 0
ans = -1
gl_flag = 1
for flat in range(1, 101):
    flag = 1
    for i in range(m):
        if not (memory[i][0] <= memory[i][1] * flat and memory[i][0] > (memory[i][1] - 1) * flat):
            flag = 0
            break
    if (flag == 1):
        #count += 1
        ans1 = (n - 1) // flat + 1
        if (ans != -1 and ans1 != ans):
            gl_flag = 0
            break
        else:
            ans = ans1 
if (gl_flag == 0):
    print(-1)
else:
    print(ans)

