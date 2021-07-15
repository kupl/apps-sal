n = int(input())
for i in range(n):
    k = int(input())
    s = 9 * (len(str(k)) - 1)
    if (len(str(k)) == 1):
        print(k)
    else:

        f = int(str(k)[0])
        if (int(str(f) * len(str(k))) > k):
            print(s + f - 1)
        else:
            print(s + f)
