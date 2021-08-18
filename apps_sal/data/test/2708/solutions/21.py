n, k = input().split()
n = list(n)[::-1]
k = int(k)

for idx, i in enumerate(n):

    if k > 0:
        i = int(i)

        if i > 0 and i >= k:
            n[idx] = str(int(n[idx]) - (k))
            k = 0
            i = int(n[idx])
            break

        elif k >= i + 1:
            n[idx] = str(0)
            k -= (i + 1)
            if k == 0:
                idx += 1
                break

    if k == 0:
        break


print(int(''.join(n[idx:][::-1])))
