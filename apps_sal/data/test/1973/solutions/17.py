def check():
    mn = float('inf')
    mx = 0
    k = 0
    for i in mas:
        if i != 0:
            k += 1
            mx = max(mx, i)
            mn = min(mn, i)
    if (mx - mn <= 1 and mas.count(mx) == 1) or (mn == 1 and k == 1 + mas.count(mx)) or (mn == mx == 1):
        return True
    return False
n = int(input())
l = list(map(int, input().split()))
mas = [0] * 10
ans = 0
for i in range(n):
    mas[l[i] - 1] += 1
    if check():
        #print(i)
        #print('check')
        ans = i
print(ans + 1)
