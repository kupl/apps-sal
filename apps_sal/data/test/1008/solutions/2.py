def sol():
    s = input()
    k = int(input())
    if len(s) % k:
        return 'NO'
    else:
        l = len(s) // k
        for i in range(k):
            st = s[i * l:(i + 1) * l]
            if st != st[::-1]:
                break
        else:
            return 'YES'
        return 'NO'


print(sol())
