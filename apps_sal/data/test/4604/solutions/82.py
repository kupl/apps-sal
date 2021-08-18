n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic.setdefault(a[i], 0)
    dic[a[i]] += 1
ans = 1
for key, value in dic.items():
    if n % 2 == 0:
        if n > key and key % 2 == 1 and value == 2:
            ans *= 2
        else:
            ans = 0
            break
    else:
        if n > key and key % 2 == 0:
            if key == 0 and value == 1:
                ans *= 1
            elif value == 2:
                ans *= 2
            else:
                ans = 0
                break
        else:
            ans = 0
            break
print(ans % (10**9 + 7))
