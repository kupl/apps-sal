import sys
N = int(input())
if N == 1:
    print(0)
    return


def prime2(N):
    arr = []
    temp = N
    setprime = set()
    for i in range(2, int(-(-N**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            setprime.add(i)
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
        setprime.add(temp)

    if arr == []:
        arr.append([N, 1])

    return arr, setprime


arr, _ = prime2(N)
ls = []
ans = 0
for i in arr:
    ls.append(i[1])
for j in ls:
    k = 1
    ii = 0
    while j >= k:
        j -= k
        k += 1
        ii += 1
    ans += ii
print(ans)
