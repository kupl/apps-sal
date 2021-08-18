h, w = list(map(int, input().split()))
'''arr = [[0] * w for i in range(h)]
arr[0] = [1] * w
for i in range(1,h):
    arr[i][0] = 1'''
mod = 1000000007
arrr = list(map(int, input().split()))
arrc = list(map(int, input().split()))

ans = 1
for i in range(h):
    for j in range(w):
        if j > arrr[i]:
            break
        elif j == arrr[i]:
            if arrc[j] > i:
                ans = 0
                break
        elif arrc[j] == i:
            ans = 0
            break
    if ans == 0:
        break
else:
    for j in range(w):
        for i in range(h):
            if i > arrc[j]:
                break
            elif i == arrc[j]:
                if arrr[i] > j:
                    ans = 0
                    break
            elif arrr[i] == j:
                ans = 0
                break
        if ans == 0:
            break
if ans == 1:
    for i in range(1, h):
        for j in range(1, w):
            if j > arrr[i] and i > arrc[j]:
                ans *= 2
                if ans > mod:
                    ans -= mod
print(ans)
