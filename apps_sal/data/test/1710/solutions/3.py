# https://codeforces.com/problemset/problem/992/D
n, k = map(int, input().split())
a = list(map(int, input().split()))
max_ = 10 ** 13 + 1


def get(l, r, x):
    min_ = min(l, r)
    max_ = max(l, r)

    if x <= min_:
        return x + 1

    if x <= max_:
        return min_ + 1

    return l + r + 1 - x


def solve(a, k):
    cnt = 0
    arr = [i for i, x in enumerate(a) if x > 1]
    n_ = len(arr)

    for i in range(n_ - 1):
        curS = 0
        curP = 1
        l = arr[i] if i == 0 else arr[i] - arr[i - 1] - 1

        for j in range(i, n_):
            ind = arr[j]
            curS += a[ind]
            curP *= a[ind]

            if curP > max_:
                break

            if curP % curS == 0:
                if curP // curS == k:
                    #print(arr[i], arr[j], curP, curS)
                    cnt += 1

            r = arr[j + 1] - arr[j] - 1
            x = curP // k - curS

            if curP % k == 0 and x > 0 and x <= l + r:
                #print(arr[i], arr[j], curP, curS)
                cnt += get(l, r, x)
            curS += r

    if k == 1:
        cnt += len(a) - n_
    return cnt


ans = 0
a.append(max_)
ans += solve(a, k)

print(ans)
