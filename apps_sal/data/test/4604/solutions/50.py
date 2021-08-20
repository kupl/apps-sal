n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
num_map = [0] * ((n + 2 - 1) // 2)
for i in range(n):
    num_map[a[i] // 2] += 1
res = 1
if n % 2 == 1:
    if num_map[0] != 1:
        print(0)
    else:
        for i in range(1, (n + 2 - 1) // 2):
            if num_map[i] != 2:
                print(0)
                break
            else:
                res = res * 2 % mod
        else:
            print(res)
else:
    for i in range((n + 2 - 1) // 2):
        if num_map[i] != 2:
            print(0)
            break
        else:
            res = res * 2 % mod
    else:
        print(res)
