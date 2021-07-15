def check(ar: list):
    ok = True
    for i in range(1, len(ar)):
        if ar[i] < ar[i - 1]:
            ok = False
            break
    if ok:
        return len(ar)
    else:
        return max(check(ar[:len(ar) // 2]), check(ar[len(ar) // 2:]))


n = int(input())
a = list(map(int, input().split()))
print(check(a))

