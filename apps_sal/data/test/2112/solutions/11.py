from math import ceil


def func(values, left, right, x, k, y, left_val, right_val):
    copy = values[left + 1:right]
    if len(copy) == 0:
        return 0
    copy.sort()
    if len(copy) < k:
        if copy[-1] > max(left_val, right_val):
            return -1
        else:
            return len(copy) * y
    elif x <= k * y:
        return len(copy) // k * x + (len(copy) % k) * y
    else:
        if copy[-1] > max(left_val, right_val):
            return x + y * (len(copy) - k)
        else:
            return y * len(copy)


def main():
    n, m = map(int, input().split())
    x, k, y = map(int, input().split())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    if m > n:
        print(-1)
    else:
        j = 0
        l = -1
        ans = 0
        for i in range(n):
            if j == m:
                break
            if s1[i] == s2[j]:
                j += 1
                if l == -1:
                    left_val = -1
                else:
                    left_val = s1[l]
                a = func(s1, l, i, x, k, y, left_val, s1[i])
                if a == -1:
                    ans = -1
                    break
                ans += a
                l = i

        if j < m or ans == -1:
            print(-1)
        else:
            a = func(s1, l, n, x, k, y, s1[l], -1)
            if a == -1:
                print(-1)
            else:
                ans += a
                print(ans)


main()
