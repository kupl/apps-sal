n = int(input())
for i in range(n):
    a = input()
    k = 9 * (len(a) - 1)
    k += int(a[0])
    s = int(a[0] * len(a))
    if int(a) < s:
        k -= 1
    print(k)
