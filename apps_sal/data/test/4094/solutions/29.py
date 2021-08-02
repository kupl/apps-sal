K = int(input())
mod = 7
for i in range(K):
    mod = mod % K
    if(mod == 0):
        print(i + 1)
        return
    else:
        mod *= 10
        mod += 7
print("-1")
