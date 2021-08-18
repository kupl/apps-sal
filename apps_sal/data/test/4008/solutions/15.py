color = []
ans = []
check = True

for _ in range(5005):
    color.append({})

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
index = 0

for i in range(N):
    k = 0
    while 1:
        try:
            color[index][arr[i]]
            index += 1
            index %= K
            k += 1
        except:
            color[index][arr[i]] = 1
            ans.append(index + 1)
            index += 1
            index %= K
            break

        if k > K:
            print("NO")
            check = False
            break
    if check == False:
        break

if check:
    print("YES")
    print(*ans)
